"""
Users = [
  {"name": "Pranav", "userId":1},
  {"name":"John", "userId":3},
  {"name":"Mash", "userId":2}
]
How can i get from Users to UserMapping in Python
Usermapping  = {1: "Pranav", 3: "John", "2": "Mash"}
"""


def convert_dict(users):
    dictUsers = dict()

    for user in users:
        dictUsers[user["userId"]] = user["name"]

    dictUsers = {user["userId"]: user["name"] for user in users}

    return dictUsers


"""
Write a function that takes two sorted arrays, and returns a
sorted array that contains all elements from both arrays.
You cannot use any js/python built in functions

Examples:
f([3, 5, 7], [0, 1, 9]) = [0, 1, 3, 5, 7, 9]
f([], [1, 2]) = [1, 2]
f([0, 1, 2], [3, 4, 5]) = [0, 1, 2, 3, 4, 5]
f([1, 2], []) = [1, 2]
"""


def join_sorted_list(list1, list2):
    resultList = []

    while list1 and list2:
        if list1[0] < list2[0]:
            resultList.append(list1.pop(0))

        else:
            resultList.append(list2.pop(0))

    return resultList + list1 + list2


list1 = [1, 3, 5]
list2 = [2, 4, 6]

join_list_result = join_sorted_list(list1, list2)
print("join_list_result", join_list_result)

users = [
    {"name": "Pranav", "userId": 1},
    {"name": "John", "userId": 3},
    {"name": "Mash", "userId": 2},
]

convert_dict_result = convert_dict(users)
print("convert_dict_result", convert_dict_result)
