# coding=utf-8
# created at 3/21/2018

import logging

__author__ = 'Chung HD'
_logger = logging.getLogger(__name__)

from dicttoxml import dicttoxml


def customer_item_func(parent):
    if parent == "Customers":
        return 'Customer'
    return "Item"

data = {"Customers":[{"name":"abc", "email":"abc@gmail", "hello":["abc"]}, {"name":"def", "email":"def@gmail"}]}

xml_str = dicttoxml(data, root=False, attr_type=False, custom_root='Customers', item_func=customer_item_func)

print(xml_str)