# python3

import sys
import threading
from collections import namedtuple

node_level = namedtuple("node_level", ["node", "level"])


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, key):
        self.items.append(key)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return self.items == []


class Node(object):
    def __init__(self, data: int, parent: int = None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, index: int):
        self.children.append(index)


class Tree(object):
    def __init__(self, parents: list):
        self.nodes = []
        self.parents = parents
        self.__build_tree()

    def __initialize_nodes(self):
        for ii in range(len(self.parents)):
            if self.parents[ii] != -1:
                self.nodes.append(Node(ii, self.parents[ii]))
            else:
                self.root = ii
                self.nodes.append(Node(ii))

    def __add_children(self):
        for ii in range(len(self.parents)):
            if self.parents[ii] == -1:
                continue
            else:
                self.nodes[self.parents[ii]].add_child(ii)

    def __build_tree(self) -> list:
        self.__initialize_nodes()
        self.__add_children()

    def compute_height(self) -> int:
        root_level = 1
        queue = Queue()
        queue.enqueue(node_level(self.root, root_level))
        max_level = 0
        while not queue.is_empty():
            node = queue.dequeue()
            if node.level > max_level:
                max_level = node.level
            for child in self.nodes[node.node].children:
                queue.enqueue(node_level(child, node.level + 1))
        return max_level


# def compute_height(n, parents):
#     # Replace this code with a faster implementation
#     max_height = 0
#     for vertex in range(n):
#         height = 0
#         current = vertex
#         while current != -1:
#             height += 1
#             current = parents[current]
#         max_height = max(max_height, height)
#     return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = Tree(parents)
    print(tree.compute_height())


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
