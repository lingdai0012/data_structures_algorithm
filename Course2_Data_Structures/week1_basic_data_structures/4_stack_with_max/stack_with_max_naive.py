# python3
import sys
import math

def binary_search

class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__sorted_stack_index = []

    def Push(self, a):
        self.__stack.append(a)
        new_index = self.size()-1
        


    def Pop(self):
        assert len(self.__stack)
        last_element = self.__stack.pop()
        if last_element  == self.__max:
            if self.__max_num > 1:
                self.__max_num -= 1
            else:
                self.

    def Max(self):
        assert len(self.__stack)
        return max(self.__stack)

    def size(self):
        return len(self.__stack)

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
