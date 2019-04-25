from copy import deepcopy

from django.db import models
# products = {product_id:count}
# Create your models here.
from merchandise.models import STORE_NAME

customer_balance = {}


def get_balance(customer):
    if customer not in customer_balance :
        customer_balance [customer] = 1000
    return customer_balance [customer]


def set_balance(customer, balance):
    customer_balance[customer] = balance


set_balance('Fang', 0)
set_balance(STORE_NAME, 0)
