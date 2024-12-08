"""Designer PDF Viewer
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""


def designerPdfViewer(h, word):
    maxLetter = -1
    for letter in word:
        index = ord(letter) - 97

        maxLetter = max(maxLetter, h[index])

    return maxLetter * len(word)


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = "abc"
print(designerPdfViewer(h, word))
