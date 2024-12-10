"""Queue using Two Stacks
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""


class QueueStack:
    def __init__(self) -> None:
        self.q = []
        self.s = []

    def enqueue(self, value):
        self.q.append(value)

    def print(self):
        if len(self.q):
            print(self.q[0])

    def dequeue(self):
        if len(self.q):
            self.q.pop(0)


queries = input()
queueStack = QueueStack()

for _ in range(int(queries)):
    querie = input().split()

    if querie[0] == "1":
        queueStack.enqueue(int(querie[1]))
    elif querie[0] == "2":
        queueStack.dequeue()
    elif querie[0] == "3":
        queueStack.print()
