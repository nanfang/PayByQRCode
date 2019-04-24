import base64
from io import BytesIO

from django.shortcuts import render
import qrcode
from django.utils.http import urlencode
from .models import products, STORE_NAME


def index(request):
    current_customer = 'Fang'
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
