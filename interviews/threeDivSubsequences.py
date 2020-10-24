'''
You are given a positive integer represented as a string number. Your task is to count the number of its substrings that form an integer divisible by 3. The substring must not have any leading zeros unless it's a single-character substring "0".

Example

For number = "456", the output should be threeDivSubsequences(number) = 3.

Let's consider all substrings of the given string:

number[0..0] = 4 isn't divisible by 3.
number[1..1] = 5 isn't divisible by 3.
number[2..2] = 6 is divisible by 3.
number[0..1] = 45 is divisible by 3.
number[1..2] = 56 isn't divisible by 3.
number[0..2] = 456 is divisible by 3.
There are 3 substrings that meet the conditions, so the answer is 3.

For number = "6666", the output should be threeDivSubsequences(number) = 10.

All substrings are divisible by 3 and have no leading zeros, so the answer is equal the number of possible substrings, which is 10.

For number = "303", the output should be threeDivSubsequences(number) = 5.

number[0..0] = 3 is divisible by 3.
number[1..1] = 0 is divisible by 3.
number[2..2] = 3 is divisible by 3.
number[0..1] = 30 is divisible by 3.
number[1..2] = 03 is divisible by 3, but it has leading zeroes, so we don't count it.
number[0..2] = 303 is divisible by 3.
There are 5 substrings that meet the conditions, so the answer is 5.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string number

An integer in the form of a string.

Guaranteed constraints:
2 ≤ number.length ≤ 10,
10 ≤ (int)number ≤ 109.

[output] integer

Return the number of substrings that form an integer divisible by 3.
'''
def numIsDivisibleByThree(numInt):
	return not bool(numInt % 3)

def deleteDuplicates(intNumbers):
	return list(dict.fromkeys(intNumbers))

def convertToInt(strNumbers):
	intNumbers = []

	for strNum in range(0, len(strNumbers)): 
		intNumbers.append(int(strNumbers[strNum]))

	return deleteDuplicates(intNumbers)

def getAllSubStrings(str):
	numsInStr = [str[start:end] for start in range(len(str)) for end in range(start+1, len(str)+1)]
	return convertToInt(numsInStr)

def threeDivSubsequences(number):
	counter = 0
	for subNum in getAllSubStrings(number):
		if numIsDivisibleByThree(subNum):
			# print(subNum)
			counter += 1
	return counter

# print(getAllSubStrings("303"))
print(threeDivSubsequences("303"))
