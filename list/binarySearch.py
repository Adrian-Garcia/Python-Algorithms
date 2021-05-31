def binarySearch(arr, target):

    low = 0
    top = len(arr) - 1

    while low <= top:

        mid = (top + low) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            top = mid - 1

        else:
            return mid

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
print("{} found at position {}".format(target, binarySearch(arr, target)))
