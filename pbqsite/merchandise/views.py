import base64
from io import BytesIO

from django.shortcuts import render
import qrcode
from django.utils.http import urlencode
from .models import products


def index(request):
    codes = {}
    for product in products:
        scheme = request.is_secure() and "https" or "http"
        pay_url = '%s://%s/pay/?%s' % (scheme, request.get_host(),
                                       urlencode({
                                           'to': 'Merchandise Store',
                                           'product_id': product.id,
                                           'product_name': product.name,
                                           'pay_for': 'Fang',
                                       }))
        img = qrcode.make(pay_url)
        buffered = BytesIO()
        img.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
        codes[product.id] = img_str

    return render(request, 'merchandise/index.html', {'products': products, 'codes': codes})
