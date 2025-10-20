"""
Decorators
    Let you add extra behavior to a function, without changing the function's code.
    A decorator is a function that takes another function as input and returns a new function.
"""


def decorator_method(function_used_within_decorator):
    print("This will be printed first")
    print(function_used_within_decorator())
    print("This will be printed third")


@decorator_method
def function_with_decorator():
    return "This will be printed second"


function_with_decorator


"""
It is widely used to format data
"""

import time
import datetime


def format_date(get_date):
    return datetime.datetime.fromtimestamp(get_date())


@format_date
def get_current_time():
    # This will return the format in miliseconds, something like 1760483087
    return time.time()


print(f"todays date is {get_current_time}")
