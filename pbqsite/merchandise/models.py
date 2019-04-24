STORE_NAME = 'Merchandise Store'


class Product(object):
    def __init__(self, id, name, price, image, count):
        self.count = count
        self.id = id
        self.name = name
        self.price = price
        self.image = image


products = [
    Product(0, 'Nice Grill', 100, 'https://i5.walmartimages.ca/images/Large/438/0-1/999999-628915624380-1.jpg', 30),
    Product(1, 'Powerful Drill', 50, 'https://images-na.ssl-images-amazon.com/images/I/41wMLiA2pyL._SX300_QL70_.jpg',
            20),
    Product(2, 'Outdoor Sofa', 250,
            'https://secure.img2-fg.wfcdn.com/im/25305293/resize-h310-w310%5Ecompr-r85/7216/72169896/belton-patio-sofa-with-cushions.jpg',
            10),
    Product(3, 'Rice Cooker', 30,
            'https://i5.walmartimages.ca/images/Large/677/551/6000198677551.jpg',
            100),
]

customer_orders = {}


def get_customer_orders(customer):
    if customer not in customer_orders:
        customer_orders[customer] = {}
    return customer_orders[customer]


def deliver_product(pay_for, product_id):
    orders = get_customer_orders(pay_for)
    orders[product_id] = dict.get(orders, product_id, 0) + 1
    products[product_id].count = products[product_id].count - 1
