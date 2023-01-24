def countPairs(numbers, k):
    a = set()

    for b in numbers:
        a.add(b - k)

    return len(a.intersection(numbers))


numbers = [1, 2]
k = 0
res = countPairs(numbers, k)
print(res)
