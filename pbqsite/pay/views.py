import json
from django.shortcuts import render
from django.views import View
import channels.layers
from asgiref.sync import async_to_sync

from merchandise.models import products, deliver_product, get_customer_orders
from pay.models import get_balance, set_balance


def transaction(pay_for, pay_from, pay_to, product):
    set_balance(pay_from, get_balance(pay_from) - product.price)
    set_balance(pay_to, get_balance(pay_to) + product.price)
    deliver_product(pay_for, product.id)


class PayView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.channel_layer = channels.layers.get_channel_layer()

    def get(self, request, *args, **kwargs):
        # /pay/?pay_to=Merchandise+Store&product_id=2&product_name=Powerful+Drill&pay_for=Fang
        return render(request, 'pay/pay_form.html', dict(
            pay_to=request.GET['pay_to'],
            product=products[int(request.GET['product_id'])],
            pay_for=request.GET['pay_for'],
            pay_from=request.GET.get('pay_from', ''),
        ))

    def post(self, request, *args, **kwargs):
        pay_for = request.POST['pay_for']
        pay_from = request.POST['pay_from']
        pay_to = request.POST['pay_to']
        product = products[int(request.GET['product_id'])]

        transaction(pay_for, pay_from, pay_to, product)

        async_to_sync(self.channel_layer.group_send)('PAYMENT_CHANNEL_GROUP',
                                                     {
                                                         'type': 'payment_message',
                                                         'message': json.dumps(
                                                             {'pay_for': pay_for,
                                                              'pay_from': pay_from,
                                                              'pay_to': pay_to,
                                                              'product_id': product.id,
                                                              'product_count': product.count,
                                                              }),
                                                     }, )

        return render(request, 'pay/pay_result.html', dict(
            pay_for=pay_for,
            pay_from=pay_from,
            pay_to=pay_to,
            product=product,
        ))


class PayStatsView(View):
    def get(self, request, *args, **kwargs):
        # /pay/?pay_to=Merchandise+Store&product_id=2&product_name=Powerful+Drill&pay_for=Fang
        customer = request.GET['customer']
        orders = get_customer_orders(customer)
        balance = get_balance(customer)
        return render(request, 'pay/pay_stats.html', dict(
            balance=balance, customer=customer, orders=[(products[p_id], count) for p_id, count in orders.items()]
        ))
