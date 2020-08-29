from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

print("Inital deque: ", q)

print("Elements dequeued from left: ", end='')
print(q.popleft(), end=' ') # [1, 2, 3]
print(q.popleft(), end=' ') # [2, 3]
print(q.popleft(), end=' ') # [3]

q.appendleft('c')
q.appendleft('b')
q.appendleft('a')

print("\n\nNew deque: ", q)
print("Elements pop dequeued (from right): ", end='')
print(q.pop(), end=' ') # [a, b, c]
print(q.pop(), end=' ') # [a, b]
print(q.pop(), end=' ') # [a]
print()