def frequencyOfMaxNewUsers(numbers, q):
    result = []
    for i in range(len(q)):
        curr_list = numbers[q[i] - 1 :]
        biggest_num = max(curr_list)
        concurrencies = curr_list.count(biggest_num)

        result.append(concurrencies)

    return result


numbers = [2, 1, 2]
q = [1, 2, 3]
res = frequencyOfMaxNewUsers(numbers, q)
print(res)
