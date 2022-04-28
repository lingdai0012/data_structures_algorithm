# python3
import math


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    for ii in range(len(data) - 1, -1, -1):
        sift_up(ii, data, swaps)
    return swaps


def sift_up(ii, data, swaps):
    if ii == 0:
        return
    parent = (ii - 1) // 2
    if data[parent] > data[ii]:
        data[parent], data[ii] = data[ii], data[parent]
        swaps.append((parent, ii))
        sift_up(parent, data, swaps)
    else:
        return


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
