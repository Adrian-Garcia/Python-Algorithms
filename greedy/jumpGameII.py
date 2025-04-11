from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res

    def jumpDoesNotWork(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return 0

        ranges = [(0, 0)]

        size = len(nums)

        while True:
            currRange = ranges[len(ranges) - 1]

            rangeStart = currRange[1] + 1
            rangeEnd = rangeStart

            for i in range(currRange[0], currRange[1] + 1):

                if i >= size:
                    continue

                print("nums                 ", nums)
                print("ranges               ", ranges)
                print("currRange            ", currRange)
                print("nums[i]              ", nums[i])
                print("rangeStart           ", rangeStart)
                print("rangeEnd 0           ", rangeEnd)

                rangeEnd = max(rangeEnd, i + nums[i])

                print("rangeEnd 1           ", rangeEnd)
                print()

                if rangeEnd >= size:
                    return len(ranges)

            # print("ranges         ", ranges)
            # print("rangeStart       ", rangeStart)
            # print("rangeEnd         ", rangeEnd)
            print()

            ranges.append((rangeStart, rangeEnd))


solution = Solution()

# nums1 = [2,4,1,1,1,1]
# res1 = solution.jump(nums1)
# print("res1", res1)

# nums2 = [2,4,1,1,1,1]
# res2 = solution.jump(nums2)
# print("res2", res2)

nums3 = [1, 1, 1, 1]
res3 = solution.jump(nums3)
print("res3", res3)
