# python3
import math
from collections import namedtuple


class Stack(object):
    def __init__(self):
        self.__items = []

    def push(self, key):
        self.__items.append(key)

    def pop(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def is_empty(self):
        return self.__items == []

    def peek(self):
        return self.__items[-1]


class Queue(object):
    def __init__(self):
        self.__s1 = Stack()
        self.__s2 = Stack()
        self.__max_s1 = []
        self.__max_s2 = []

    def enqueue(self, key):
        self.__s2.push(key)
        if len(self.__max_s2) == 0:
            self.__max_s2.append(key)
        else:
            if key > self.__max_s2[-1]:
                self.__max_s2.append(key)
            else:
                self.__max_s2.append(self.__max_s2[-1])

    def dequeue(self):
        if self.__s1.is_empty():
            while not self.__s2.is_empty():
                recent_items = self.__s2.pop()
                self.__s1.push(recent_items)
                if self.__max_s1 == []:
                    self.__max_s1.append(recent_items)
                else:
                    if recent_items > self.__max_s1[-1]:
                        self.__max_s1.append(recent_items)
                    else:
                        self.__max_s1.append(self.__max_s1[-1])

            self.__max_s2 = []
        popped_item = self.__s1.pop()
        self.__max_s1 = self.__max_s1[:-1]
        return popped_item

    def peek(self):
        return self.__s1.peek()

    def is_empty(self):
        return self.__s1.is_empty()

    def size(self):
        return self.__s1.size()

    def max(self):
        if len(self.__max_s1) == 0:
            return self.__max_s2[-1]
        if len(self.__max_s2) == 0:
            return self.__max_s1[-1]
        return max(self.__max_s2[-1], self.__max_s1[-1])


def max_sliding_window(sequence, m):
    maximums = []
    queue = Queue()
    for ii in range(m - 1):
        queue.enqueue(sequence[ii])

    for ii in range(m - 1, len(sequence)):
        queue.enqueue(sequence[ii])
        maximums.append(queue.max())
        _ = queue.dequeue()
    return maximums


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i : i + m]))

    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
