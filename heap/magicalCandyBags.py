"""Magical Candy Bags
https://www.metacareers.com/profile/coding_practice_question/?problem_id=513590792640579&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122

You have N bags of candy. The ith bag contains arr[i] pieces of candy, and
each of the bags is magical!

It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective
of how many pieces of candy are inside), and as soon as you finish, the bag
mysteriously refills. If there were x pieces of candy in the bag at the
beginning of the minute, then after you've finished you'll find that floor(x/2)
pieces are now inside.

You have k minutes to eat as much candy as possible. How many pieces of candy
can you eat?

Signature
    int maxCandies(int[] arr, int K)

Input
    1 ≤ N ≤ 10,000
    1 ≤ k ≤ 10,000
    1 ≤ arr[i] ≤ 1,000,000,000

Output
    A single integer, the maximum number of candies you can eat in k minutes.

Example 1
    N = 5 
    k = 3
    arr = [2, 1, 7, 4, 2]
    output = 14

    In the first minute you can eat 7 pieces of candy. That bag will refill
    with floor(7/2) = 3 pieces.

    In the second minute you can eat 4 pieces of candy from another bag. That
    bag will refill with floor(4/2) = 2 pieces.
    
    In the third minute you can eat the 3 pieces of candy that have appeared in
    the first bag that you ate.
    
    In total you can eat 7 + 4 + 3 = 14 pieces of candy.
"""
import heapq


def maxCandies(arr, k):

    count = 0

    for _ in range(k):
        heapq._heapify_max(arr)
        arr = list(arr)
        maxCandy = arr.pop(0)
        count += maxCandy
        arr.append(maxCandy // 2)

    return count


arr1 = [2, 1, 7, 4, 2]
arr2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
print(maxCandies(arr1, 3))
print(maxCandies(arr2, 3))
