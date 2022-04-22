# python3
import sys
import math


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__maxs = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__maxs) == 0:
            self.__maxs.append(a)
        else:
            if a > self.__maxs[-1]:
                self.__maxs.append(a)
            else:
                self.__maxs.append(self.__maxs[-1])

    def Pop(self):
        assert len(self.__stack)
        self.__stack.pop()
        self.__maxs.pop()

    def Max(self):
        assert len(self.__stack)
        return self.__maxs[-1]


if __name__ == "__main__":
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
