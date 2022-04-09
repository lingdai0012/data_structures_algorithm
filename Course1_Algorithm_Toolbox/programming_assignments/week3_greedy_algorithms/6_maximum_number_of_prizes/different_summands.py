# Uses python3
import sys


def optimal_summands(n):
    summands = []
    remainer = n
    # write your code here
    for i in range(1, n + 1):
        if (remainer > 2 * i) or (remainer == i):
            summands.append(i)
            remainer -= i
            if remainer == 0:
                break
        else:
            continue

    return summands


if __name__ == "__main__":
    # input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
