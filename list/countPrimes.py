"""
204. Count Primes
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
    Input: n = 0
    Output: 0
    Example 3:

Example 3:
    Input: n = 1
    Output: 0
 
Constraints:
    0 <= n <= 5 * 106


                 x
primes[0] = list(2,3,4,5,6,7,8,9)
                   x
primes[1] = list(2,3,5,7,9)
                     x
primes[2] = list(2,3,5,7)
                       x
primes[3] = list(2,3,5,7)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = list(range(2, n))
        i = 0

        while i < len(primes):

            new_primes = []
            curr_num = primes[i]

            for num in primes:
                if curr_num == num:
                    new_primes.append(num)

                elif num % curr_num != 0:
                    new_primes.append(num)

            primes = new_primes
            i += 1

        return len(primes)


solution = Solution()
res1 = solution.countPrimes(10)
print("res1", res1)
