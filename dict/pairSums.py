"""Pair Sums
https://www.metacareers.com/profile/coding_practice_question/?problem_id=840934449713537&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122

       i
arr = [1, 2, 3, 4, 3]

count = 4 / 2 = 2
k = 6


{1,2,3,4}
{
    1:[0]
    2:[1]
    3:[2,3]
    4:[3]
}

"""


def numberOfWays(arr, k):
    count = 0
    numbers = dict()

    for i in range(len(arr)):
        num = arr[i]

        if num in numbers:
            numbers[num].add(i)
        else:
            numbers[num] = set([i])

    for i in range(len(arr)):
        diff = k - arr[i]

        if diff in numbers and len(numbers[diff].difference(set([i]))) >= 1:
            count += 1

        print("arr                                      ", arr)
        print("k                                        ", k)
        print("numbers                                  ", numbers)
        print("i                                        ", i)
        print("arr[i]                                   ", arr[i])
        print("diff                                     ", diff)
        print("count                                    ", count)
        print(
            "numbers[diff].difference(set([i]))    ", numbers[diff].difference(set([i]))
        )

    return count


arr1 = [1, 2, 3, 4, 3]
arr2 = [1, 5, 3, 3, 3]

# print(numberOfWays(arr1, 6))
print(numberOfWays(arr2, 6))
