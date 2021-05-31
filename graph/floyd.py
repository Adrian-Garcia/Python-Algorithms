inf = float("inf")


def floyd(D, n):

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] != inf and D[k][j] != inf and D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]

    return D


D = [
    [0, 5, inf, 1, inf],
    [5, 0, 2, inf, 1],
    [inf, 2, 0, inf, 8],
    [1, inf, inf, 0, inf],
    [inf, 1, 8, inf, 0],
]

print(floyd(D, 5))
