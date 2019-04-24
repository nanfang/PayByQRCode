import base64
from io import BytesIO

from django.shortcuts import render
import qrcode
from django.utils.http import urlencode


def index(request):
    products = []
    for i in [1, 2]:
        product = {
            'id': i,
            'name': 'Product %s' % i,
        }
        scheme = request.is_secure() and "https" or "http"
        pay_url = '%s://%s/pay/?%s' % (scheme, request.get_host(), urlencode({'to': 'Merchandise Store'}))
        img = qrcode.make(pay_url)
        buffered = BytesIO()
        img.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
        product['qrcode'] = img_str

        products.append(product)

    return render(request, 'merchandise/index.html', {'products': products})

