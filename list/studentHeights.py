def solution(A):

    if len(A) == 0:
        return 0

    maxNum = A[0]
    numRows = 1

    for element in A:

        if element > maxNum:
            numRows += 1
            maxNum = element

    return numRows


print(solution([5, 4, 3, 6, 1]))
