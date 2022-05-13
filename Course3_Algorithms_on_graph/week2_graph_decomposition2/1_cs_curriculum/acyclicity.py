# Uses python3

import sys


def acyclic(adj):
    for ii in range(len(adj)):
        if reachability(ii, ii, adj) == 1:
            return 1
    return 0


def reachability(ii, target_ii, adj):
    if adj[ii] is None:
        return 0
    else:
        if target_ii in adj[ii]:
            return 1
        else:
            nexts = adj[ii]
            adj[ii] = None
            for jj in nexts:
                if reachability(jj, target_ii, adj) == 1:
                    return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
