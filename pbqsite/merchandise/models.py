from django.db import models


class Product(object):
    def __init__(self, id, name, price, image, count):
        self.count = count
        self.id = id
        self.name = name
        self.price = price
        self.image = image


products = [
    Product(1, 'Nice Grill', 100, 'https://i5.walmartimages.ca/images/Large/438/0-1/999999-628915624380-1.jpg', 100),
    Product(2, 'Powerful Drill', 50, 'https://images-na.ssl-images-amazon.com/images/I/41wMLiA2pyL._SX300_QL70_.jpg',
            20),
    Product(3, 'Outdoor Sofa', 250,
            'https://secure.img2-fg.wfcdn.com/im/25305293/resize-h310-w310%5Ecompr-r85/7216/72169896/belton-patio-sofa-with-cushions.jpg',
            10)
]
