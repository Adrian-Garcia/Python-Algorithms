"""Largest Triple Products
https://www.metacareers.com/profile/coding_practice_question/?problem_id=510655302929581&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122
"""


def findMaxProduct(arr):
    if len(arr) < 3:
        return [-1] * len(arr)

    response = [-1, -1]

    for i in range(len(arr) - 2):
        j = i + 3

        window = arr[:j]
        window.sort()
        product = 1

        for _ in range(3):
            product *= window.pop()

        response.append(product)

    return response


arr = [1, 2, 3, 4, 5]
print(findMaxProduct(arr))
