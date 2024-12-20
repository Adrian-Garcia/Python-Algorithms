"""Rotational Cipher
https://www.metacareers.com/profile/coding_practice_question/?problem_id=238827593802550&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122

One simple way to encrypt a string is to "rotate" every alphanumeric character by a
certain amount. Rotating a character means replacing it with another character that
is a certain number of steps away in normal alphabetic or numerical order.

For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is
"Cheud-726?". Every alphabetic character is replaced with the character 3 letters
higher (wrapping around from Z to A), and every numeric character replaced with the
character 3 digits higher (wrapping around from 9 to 0). Note that the
non-alphanumeric characters remain unchanged.

Given a string and a rotation factor, return an encrypted string.

Signature
    string rotationalCipher(string input, int rotationFactor)

Input
    1 <= |input| <= 1,000,000
    0 <= rotationFactor <= 1,000,000

Output
    Return the result of rotating input a number of times equal to rotationFactor.

Example 1
    input = Zebra-493?
    rotationFactor = 3
    output = Cheud-726?

Example 2
    input = abcdefghijklmNOPQRSTUVWXYZ0123456789
    rotationFactor = 39
    output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""


def cipherCharacter(char: str, baseChar: str, rotationFactor, numberOfChars) -> str:
    return chr(
        (ord(char) - ord(baseChar) + rotationFactor % numberOfChars) % numberOfChars
        + ord(baseChar)
    )


def rotationalCipher(input_str: str, rotation_factor: int) -> str:
    outputStr = ""

    for char in input_str:
        if ord("0") <= ord(char) <= ord("9"):
            outputStr += cipherCharacter(char, "0", rotation_factor, 10)

        elif ord("a") <= ord(char) <= ord("z"):
            outputStr += cipherCharacter(char, "a", rotation_factor, 26)

        elif ord("A") <= ord(char) <= ord("Z"):
            outputStr += cipherCharacter(char, "A", rotation_factor, 26)

        else:
            outputStr += char

    return outputStr


print(rotationalCipher("0123456789", 11))
print(rotationalCipher("abcdefghijklmnopqrstuvwxyz", 27))
print(rotationalCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 27))

print(rotationalCipher("Zebra-493", 3))
print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))
