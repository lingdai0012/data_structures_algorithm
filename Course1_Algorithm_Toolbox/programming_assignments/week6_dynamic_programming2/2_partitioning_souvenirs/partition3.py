# Uses python3
import sys
import itertools
import time
import random


def naive_partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0


def partition3(A: list) -> bool:
    A_sum = sum(A)
    if A_sum % 3 != 0:
        return 0
    A_sum_one_third = A_sum // 3
    sorted_A_index = sorted(list(range(len(A))), reverse=True, key=lambda ii: A[ii])
    bag1, bag2, bag3 = (
        A_sum_one_third - A[sorted_A_index[0]],
        A_sum_one_third,
        A_sum_one_third,
    )

    def top_down_dp(index, bag, used_items, all_items):
        if bag == 0:
            if used_items not in all_items:
                all_items.append(used_items)
        if len(index) > 0:
            top_down_dp(
                index[1:],
                bag - A[index[0]],
                used_items.union({index[0]}),
                all_items,
            )
            top_down_dp(index[1:], bag, used_items, all_items)
        return all_items

    def match(index, bag):
        if bag == 0:
            return 1
        if (bag < 0) or (len(index) == 0):
            return 0
        return max(match(index[1:], bag - A[index[0]]), match(index[1:], bag))

    used_items_1 = set()
    all_used_items_1 = []
    all_used_items_1 = top_down_dp(sorted_A_index, bag1, used_items_1, all_used_items_1)
    for used_items_1 in all_used_items_1:
        not_used_index = [ii for ii in sorted_A_index if ii not in used_items_1]
        if match(not_used_index, bag2) == 1:
            return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
