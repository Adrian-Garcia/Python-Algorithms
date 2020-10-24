'''
For the given string s, and array of strings a, s is said to be a prefix-string of a if it is a concatenation of some prefix of the array a, i.e. if there exists some index i, such that s = a[0] + a[1] + ... + a[i].
For example, for a = ["one", "two", "three"] strings s = "one" and s = "onetwo" are prefix-strings, while s = "two", s = "onetw", and s = "onethree" are not.

Given two arrays of strings a and b, your task is to determine whether all the given strings in b are prefix-strings of a.

Example

For a = ["one", "two", "three"] and b = ["onetwo", "one"], the output should be prefixStrings(a, b) = true.

Both of the strings b[0] = "onetwo" and b[1] = "one" are prefix-strings of a.

For a = ["One", "TwoThree", "Four"] and b = ["One", "OneTwo"], the output should be prefixStrings(a, b) = false.

The second string b[1] = "OneTwo" is not a prefix-string of a, since it doesn't fully match the concatenated elements of a ("OneTwoThree" would be fine, but "OneTwo" is incomplete).

For a = ["One", "Two", "Three"] and b = ["Two"], the output should be prefixStrings(a, b) = false.

Here is the list of prefix-strings:

"One",
"OneTwo",
"OneTwoThree".
"Two" isn't an option, so return false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string a

An array of strings. It is guaranteed that each its element only consist of English letters.

Guaranteed constraints:
1 ≤ a.length ≤ 100,
1 ≤ a[i].length ≤ 100.

[input] array.string b

An array of strings. It is guaranteed that each its element only consist of English letters.

Guaranteed constraints:
1 ≤ b.length ≤ 100,
1 ≤ b[i].length ≤ 100.

[output] boolean

Return true if every element from b is prefix-string and false otherwise.
'''
def isInStr(str, substr):
	return str.find(substr) != -1

def prefixString(a, b):
	for str in b:
		myStr = str

		for subStr in a:
			deletedStr = myStr.replace(subStr, '', 1)

			if deletedStr == myStr:
				return False

			myStr = deletedStr

			if myStr == '':
				break

	return True

a = ["A", "A", "A", "A"]
b = ["AAA"]

print(prefixString(a, b))
