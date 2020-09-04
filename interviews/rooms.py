def solution(A):

  if not A:
    return 0

  mySet = set()
  for element in A:
    # It is sorted if it arrives A0 instad of 0A
    deleteSign = sorted(element[1:len(element)])
    room = ''.join(deleteSign)
    mySet.add(room)

  return len(mySet)

arr = ["+5A"]
print(solution(arr))