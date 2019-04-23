import base64
from io import BytesIO

from django.shortcuts import render
import qrcode


def index(request):
    products = []
    for i in [1, 2]:
        product = {
            'id': i,
            'name': 'Product %s' % i,
        }
        pay_url = 'https://www.amazon.com/iss/credit/storecardmember?_encoding=UTF8&plattr=PLCCFOOT&ref_=footer_plcc'
        img = qrcode.make(pay_url)
        buffered = BytesIO()
        img.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
        product['qrcode'] = img_str

        products.append(product)

    return render(request, 'merchandise/index.html', {'products': products})
