def leadingZeroes(num):
	if num == "0":
		return False
	return True if num[0] == '0' else False

def numIsDivisibleByThree(numInStr):
	return False if leadingZeroes(numInStr) else not(bool(int(numInStr) % 3))

def getAllSubStrings(str):
	return [str[start:end] for start in range(len(str)) for end in range(start+1, len(str)+1)]

def threeDivSubsequences(number):
	counter = 0
	for subNum in getAllSubStrings(number):
		if numIsDivisibleByThree(subNum):
			counter += 1
	return counter

print(threeDivSubsequences('303'))
