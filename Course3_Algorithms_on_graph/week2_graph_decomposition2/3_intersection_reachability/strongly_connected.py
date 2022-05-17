# Uses python3

import sys
from collections import namedtuple

sys.setrecursionlimit(200000)


def dfs(adj, orders, used, x, postorder):
    if used[x] == 1:
        return postorder
    else:
        used[x] = 1
        for jj in adj[x]:
            if used[jj] == 0:
                postorder = dfs(adj, orders, used, jj, postorder)
        postorder += 1
        orders[x] = postorder
    return postorder


def explore(adj, used, x):
    used[x] = 1
    for jj in adj[x]:
        if used[jj] == 0:
            explore(adj, used, jj)
    return


def number_of_strongly_connected_components(adj, adj_r):
    result = 0
    # write your code here
    orders = [None for _ in range(len(adj))]
    used = [0 for _ in range(len(adj))]
    postorder = 0
    for ii in range(len(adj_r)):
        postorder = dfs(adj_r, orders, used, ii, postorder)

    used = [0 for _ in range(len(adj))]
    sorted_orders_index = sorted(list(range(len(orders))), key=lambda ii: orders[ii])
    component = 0
    for ii in range(len(orders) - 1, -1, -1):
        if used[sorted_orders_index[ii]] != 1:
            explore(adj, used, sorted_orders_index[ii])
            component += 1
    return component


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_r[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj_r))
