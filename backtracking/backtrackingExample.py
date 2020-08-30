'''
Fails when one of the needed elements are in the last position

Given a vector and a number, return the subset of numbers that summed, return the given number
	
	Test 1
		numbers = [1,2,3]
		goal = 4

		return = [1,3] 1 + 3 = 4

	Test 2
		numbers = [1,-2,3]
		goal = -1

		return = [1,-2]
'''

result = []
counter = 1

def backtracking(numbers, goal, currentSubset, sum, index, flagToStop):

	print (counter)
	# counter = counter + 1

	if index > len(numbers)-1:
		return

	elif flagToStop:
		return

	elif sum == goal:
		flagToStop = True
		result = currentSubset
		print("EUREKA: {}".format(currentSubset))
		return

	else:
		currentSubsetSame = currentSubset.copy()
		currentSubsetDiff = currentSubset.copy()
		currentSubsetDiff.append(numbers[index])

		backtracking(numbers, goal, currentSubsetSame, sum, index + 1, flagToStop)
		backtracking(numbers, goal, currentSubsetDiff, sum + numbers[index], index + 1, flagToStop)

class Solution(object):


	def subsets(self, numbers, goal):
		backtracking(numbers, goal, [], 0, 0, False)
		return result

sol = Solution()

print(sol.subsets([1,-2, 3], 1))