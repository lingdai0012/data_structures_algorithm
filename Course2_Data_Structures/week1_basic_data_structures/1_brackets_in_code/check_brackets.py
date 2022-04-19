# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


class Stack(object):
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, key):
        self.__items.append(key)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]


def find_mismatch(text):
    stack = Stack()
    left_brackets = ["[", "{", "("]
    right_brackets = ["]", "}", ")"]
    for ii in range(len(text)):
        if text[ii] in left_brackets:
            stack.push(Bracket(text[ii], ii))
        else:
            if text[ii] in right_brackets:
                if stack.is_empty():
                    return ii + 1
                top = stack.pop()
                if left_brackets[right_brackets.index(text[ii])] != top[0]:
                    return ii + 1
    if stack.is_empty():
        return "Success"
    else:
        while not stack.is_empty():
            first_item = stack.pop()
        return first_item[1] + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
