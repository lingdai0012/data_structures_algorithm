# python3

import sys, threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.__inOrderTraverse(0)
        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.__preOrderTraverse(0)
        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.__postOrderTraverse(0)
        return self.result

    def __inOrderTraverse(self, target_index):
        if target_index == -1:
            return
        self.__inOrderTraverse(self.left[target_index])
        self.result.append(self.key[target_index])
        self.__inOrderTraverse(self.right[target_index])

    def __preOrderTraverse(self, target_index):
        if target_index == -1:
            return
        self.result.append(self.key[target_index])
        self.__preOrderTraverse(self.left[target_index])
        self.__preOrderTraverse(self.right[target_index])

    def __postOrderTraverse(self, target_index):
        if target_index == -1:
            return
        self.__postOrderTraverse(self.left[target_index])
        self.__postOrderTraverse(self.right[target_index])
        self.result.append(self.key[target_index])


def main():
    tree = TreeOrders()
    tree.read()

    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
