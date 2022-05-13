# Uses python3

import sys


def dfs(adj, used, order, x):
    # write your code here
    for jj in adj[x]:
        if used[jj] == 0:
            dfs(adj, used, order, jj)

    if used[x] == 0:
        order.insert(0, x)
        used[x] = 1
    return


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # write your code here
    for ii in range(len(adj)):
        dfs(adj, used, order, ii)
    return order


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=" ")
