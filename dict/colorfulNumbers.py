""" 123. Colorful Numbers
https://tutorialhorizon.com/algorithms/colorful-numbers/

Objective: Given a number, find out whether it is colorful.

Colorful Number: When in a given number, the product of every contiguous sub-sequence is different.
That number is called a Colorful Number. 

Example 1:
    Given Number : 3245
    Output: Colorful

    Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
    this number is a colorful number, since product of every digit of a sub-sequence are different.
    That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

Example 2:

    Given Number : 326
    Output: Not Colorful.

    326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
    
    Approach:

        The idea is to get the product of all possible subarrays and keep storing it in a Set,
        if any time the current subarray product is already in a Set, return false, else at the end
        return true 

        Read - Print all subarrays of a given array Video - https://www.youtube.com/watch?v=xHwMaxq2Qxo
"""


def product_of_sub_sequence(arr) -> int:
    result = 1

    for num in arr:
        number = int(num)
        result *= number

    return result


def is_colorful(number: int) -> bool:
    str_number = str(number)
    products = set()
    size = len(str_number)

    for i in range(size):

        for j in range(size):
            start = j
            end = j + i + 1

            if end > size:
                continue

            product = product_of_sub_sequence(str_number[start:end])

            if product in products:
                return False

            products.add(product)

    return True


number1 = 3245  # True
number2 = 326  # False
print(is_colorful(number2))
