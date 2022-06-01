#!/usr/bin/python3

import sys, threading
import math
from collections import namedtuple


sys.setrecursionlimit(10**10)  # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if len(tree) == 0:
        return True
    answer = postOrderTraversal(tree, 0)
    return answer[0]


def postOrderTraversal(tree, index):
    if index == -1:
        return (None, None, None)
    left_is_bst, left_max, left_min = postOrderTraversal(tree, tree[index][1])
    right_is_bst, right_max, right_min = postOrderTraversal(tree, tree[index][2])
    if left_is_bst is None and right_is_bst is None:
        return (True, tree[index][0], tree[index][0])
    elif left_is_bst is None:
        return (
            tree[index][0] <= right_min and right_is_bst,
            max(tree[index][0], right_max),
            min(tree[index][0], right_min),
        )
    elif right_is_bst is None:
        return (
            left_max < tree[index][0] and left_is_bst,
            max(tree[index][0], left_max),
            min(tree[index][0], left_min),
        )
    else:
        return (
            left_max < tree[index][0] <= right_min and left_is_bst and right_is_bst,
            max(right_max, left_max, tree[index][0]),
            min(right_min, left_min, tree[index][0]),
        )


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
