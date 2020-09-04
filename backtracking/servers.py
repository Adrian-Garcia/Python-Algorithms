def backtracking(A, index, middle, closest):

	if middle < closest[0]:
		closest[0] = middle

	if middle == 0:
		return True

	if index == 0 and middle != 0:
		return False

	if A[index-1] > middle:
		return backtracking(A, index-1, middle, closest)

	return backtracking(A, index-1, middle, closest) or backtracking(A, index-1, middle-A[index-1], closest)

def getDifference(candidateForBestOption, bestOptionSoFar, targetResult):
	return abs(targetResult - candidateForBestOption) < bestOptionSoFar

def sumOfList(A):
	addition = 0

	for i in A:
		addition += i

	return addition

def solution(A):
	n = len(A)
	addition = sumOfList(A)
	middle = int(addition / 2)
	closest = [addition]

	return addition-middle*2 if backtracking(A, n, middle, closest) else closest[0]

print(solution([1,2,3,4,5]))