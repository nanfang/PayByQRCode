import base64
import qrcode
from io import BytesIO
from django.shortcuts import render, redirect
from django.utils.http import urlencode
from django.views import View
from .models import products, STORE_NAME

SESSION_KEY = 'customer'


def index(request):
    current_customer = request.session[SESSION_KEY]
    codes = {}
    for product in products:
        scheme = request.is_secure() and "https" or "http"
        pay_url = '%s://%s/pay/?%s' % (scheme, request.get_host(),
                                       urlencode({
                                           'pay_to': STORE_NAME,
                                           'product_id': product.id,
                                           'product_name': product.name,
                                           'pay_for': current_customer,
                                       }))
        img = qrcode.make(pay_url)
        buffered = BytesIO()
        img.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
        codes[product.id] = img_str

    return render(request, 'merchandise/index.html',
                  {'store_name': STORE_NAME,
                   'current_customer': current_customer,
                   'products': products,
                   'codes': codes})


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'merchandise/login.html')

    def post(self, request, *args, **kwargs):
        request.session[SESSION_KEY] = request.POST[SESSION_KEY]
        return redirect('/merchandise/')
