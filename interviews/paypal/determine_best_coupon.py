"""
Given a list of coupon codes and their discounts (expressed here as JSON; OK to enter directly into code using preferred format):

[
  {"code": "SAVE10PCT",  "discountType": "PERCENT_OFF_ORDER",   "discountAmount": 10},
  {"code": "FIVEBUXOFF", "discountType": "DOLLARS_OFF_ORDER",   "discountAmount": 5},
  {"code": "CHEAPFOO",   "discountType": "DOLLARS_OFF_PRODUCT", "discountAmount": 10, "productId": "FOO"}
]
Write a function that takes the following:

the coupons
the distinct productIds in the cart
the order subtotal
... and returns a string: the code that yields the greatest potential savings.


"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'determine_best_coupon' function below.
#
# The function is expected to return a STRING.
#
COUPONS = [
    {"code": "SAVE10PCT", "discountType": "PERCENT_OFF_ORDER", "discountAmount": 10},
    {"code": "SAVE10PCT", "discountType": "PERCENT_OFF_ORDER", "discountAmount": 20},
    {"code": "SAVE10PCT", "discountType": "PERCENT_OFF_ORDER", "discountAmount": 40},
    {"code": "FIVEBUXOFF", "discountType": "DOLLARS_OFF_ORDER", "discountAmount": 5},
    {
        "code": "CHEAPFOO",
        "discountType": "DOLLARS_OFF_PRODUCT",
        "discountAmount": 10,
        "productId": "FOO",
    },
]
cart = [
    {"productId": "BAR", "cost": 20000000000},
    {"productId": "FOO", "cost": 10},
]

"""
{
    "SAVE10PCT" : {
        "discountType": "PERCENT_OFF_ORDER",
        "discountAmount": 
    }
}
"""


def __get_coupons_list(info_coupons_list):
    coupons_list = dict()

    for coupon in info_coupons_list:
        coupons_list[coupon["code"]]: {
            "discountType": coupon["discountType"],
            "discountAmount": coupon["discountAmount"],
            "productId": coupon.get("productId"),
        }

    return coupons_list


def get_final_price(product, coupon):
    """
    calculates the best price of a product based on DOLLARS_OFF_PRODUCT coupon type
    """
    if coupon["DOLLARS_OFF_PRODUCT"] and product["productId"] == coupon["productId"]:
        return product["cost"] - coupon["discountAmount"]

    return product["cost"]


def get_bests_order_coupons(coupons):
    best_percentage = float("inf")
    best_dollars = float("inf")

    best_percentage_code = None
    best_dollars_code = None

    for coupon in coupons:
        if (
            coupon["discountType"] == "PERCENT_OFF_ORDER"
            and coupon["discountAmount"] > best_percentage
        ):
            best_percentage = coupon["discountAmount"]
            best_percentage_code = coupon["code"]

        elif (
            coupon["discountType"] == "DOLLARS_OFF_ORDER"
            and coupon["discountAmount"] > best_dollars
        ):
            best_dollars = coupon["discountAmount"]
            best_dollars_code = coupon["code"]

    return best_percentage_code, best_dollars_code


def get_discounted_money(product, coupons):
    best_price = float("inf")
    best_coupon = None

    for coupon in coupons:
        curr_price = get_final_price(product, coupon)
        if curr_price < best_price:
            best_price = curr_price
            best_coupon = coupon

    return best_coupon["code"]


def determine_best_coupon(cart, coupons):
    codes = []

    # Get codes from card
    for product in sort_cart(cart):
        codes.append(get_discounted_money(product, coupons))

    best_percentage_code, best_dollars_code = get_bests_order_coupons(coupons)

    codes.append(best_percentage_code)
    codes.append(best_dollars_code)

    return codes


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    result = determine_best_coupon()

    fptr.write(result + "\n")

    fptr.close()
