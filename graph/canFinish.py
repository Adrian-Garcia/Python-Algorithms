"""
Course Schedule
https://neetcode.io/problems/course-schedule

You are given an array prerequisites where prerequisites[i] = [a, b] indicates
that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0
to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[0,1]]
    Output: true

    Explanation:
        First take course 1 (no prerequisites) and then take course 0.

Example 2:
    Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
    Output: false

    Explanation:
        In order to take course 1 you must take course 0, and to take course 0
        you must take course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 1000
    0 <= prerequisites.length <= 1000
    All prerequisite pairs are unique.
"""

from typing import List


class Solution:
    def __visitChain(self, courseId: int, courses: dict, courseIds: set):
        visited = set()
        queue = [courseId]

        while queue:
            currCourseId = queue.pop(0)

            if currCourseId not in courses:
                continue

            prerequisites = courses[currCourseId]

            if any(ele in visited for ele in prerequisites):
                return False

            visited.add(currCourseId)
            queue += prerequisites

        courseIds -= visited
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseIds = set()
        courses = dict()

        for course in prerequisites:
            courseId = course[0]
            prerequisite = course[1]

            courseIds.add(courseId)
            if courseId in courses:
                courses[courseId].append(prerequisite)

            else:
                courses[courseId] = [prerequisite]

        for courseId in courses:
            if not self.__visitChain(courseId, courses, courseIds):
                return False

        return True


solution = Solution()

prerequisites1 = [[0, 1]]
res1 = solution.canFinish(2, prerequisites1)
print("res1", res1)

prerequisites2 = [[0, 1], [1, 0]]
res2 = solution.canFinish(2, prerequisites2)
print("res2", res2)
