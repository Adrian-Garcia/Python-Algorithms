import sys


class QHeap:
    def __init__(self) -> None:
        self.dictionary = dict()
        self.min = sys.maxsize

    def __findNewMin(self):
        self.min = sys.maxsize
        for element in self.dictionary:
            if self.dictionary[element] > 0:
                self.min = min(element, self.min)

    def add(self, v):
        if v in self.dictionary:
            self.dictionary[v] += 1

        else:
            self.dictionary[v] = 1

        self.min = min(self.min, v)

    def delete(self, v):
        if v in self.dictionary and self.dictionary[v] > 0:
            self.dictionary[v] -= 1
            if self.dictionary[v] == 0 and self.min == v:
                self.__findNewMin()

    def printMin(self):
        print(self.min)


queries = int(input())
heap = QHeap()

for _ in range(queries):
    query = input().split()

    if query[0] == "1":
        heap.add(int(query[1]))

    if query[0] == "2":
        heap.delete(int(query[1]))

    if query[0] == "3":
        heap.printMin()

"""
heap = QHeap()
heap.add(3)
heap.add(4)
heap.add(2)
heap.printMin()
heap.delete(2)
heap.printMin()
"""
