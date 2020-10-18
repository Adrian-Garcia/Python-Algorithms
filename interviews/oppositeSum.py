def oppositeSums(arr):
    dicA = {}
    dicB = {}
    aux = 0
    pairs = 0
    
    for i,v in enumerate(arr):
        for j in range(i, len(arr)):
            aux = v + rev(arr[j])
            dicA[aux] += 1
            aux = arr[j] + rev(arr[i])
            dicB[aux] += 1
            
    for x in dicA:
        if x in dicB:
            pairs += 1
            
    return pairs