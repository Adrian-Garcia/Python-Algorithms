def get_all_substrings(s):
    return [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def number_of_corrext_substrings(substrings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = 0

    for substring in substrings:
        if vowels == set(substring):
            counter += 1

    return counter

def memory_solution(s):
    substrings = get_all_substrings(s)
    return number_of_corrext_substrings(substrings)

def no_memory_solution(s):
    counter = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i in range(0, len(s)):
        for k in range(0, len(s) - i):
            substring = set(s[k:i+k+1])
            if vowels == substring:
                counter += 1

    return counter

def efficient_solution(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = 0
 
    n = len(s)
    for i in range(n):
        substr = dict()
        for j in range(i, n):
            if s[j] not in vowels:
                break
 
            substr[s[j]] = 1
 
            if (len(substr) == 5):
                counter += 1

    return counter
