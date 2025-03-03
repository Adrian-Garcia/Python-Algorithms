'''
[
    [xQx]
    [xxx]
    [Qxx]
]

[
    [xQxx]
    [xxxQ]
    [Qxxx]
    [xxxQ]
]

'''
def printBoard(board):
    n = len(board)

    for i in range(n):
        for j in range(n):
            print(board[i][j], end="")
        print()
    print()

class Solution:
    def __setQueenPath(self, board, iPosition, jPosition):
        n = len(board)
        iUp = iPosition - 1
        iDown = iPosition + 1
        jLeft = jPosition - 1
        jRight = jPosition + 1

        # up
        while iUp >= 0:
            if board[iUp][jPosition] == "Q":
                return False
            iUp -= 1

        # down
        while iDown < n:
            if board[iDown][jPosition] == "Q":
                return False
            iDown += 1

        # left
        while jLeft >= 0:
            if board[iPosition][jLeft] == "Q":
                return False
            jLeft -= 1

        # down
        while jRight < n:
            if board[iPosition][jRight] == "Q":
                return False
            jRight += 1

        # Up-Left
        # Up-Right
        # Down-Right
        # Down-Left

        return True



    def totalNQueens(self, n: int) -> int:
        originalBoard = [["."] * n for _ in range(n)]
        numberOfQueens = 0
        currQueens = 0

        """
        Qxxx
        xxQx
        xxxx
        xQxx
        """

        for i in range(n):
            for j in range(n):
                if originalBoard[i][j] == ".":
                    currQueens += 1
                    originalBoard[i][j] = "Q"
                    self.__setQueenPath(originalBoard, i, j)

        if currQueens == n:
            "YES"

solution = Solution().totalNQueens(3)

