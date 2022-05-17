# Uses python3

import sys
import queue


def bipartite(adj):
    # write your code here
    colors = [None for _ in range(len(adj))]
    q = queue.Queue()
    for ii in range(len(adj)):
        if colors[ii] is None:
            q.put(ii)
            colors[ii] = 0
            is_bipartite = bfs(adj, q, colors)
            if is_bipartite == 0:
                return 0
    return 1


def bfs(adj, q, colors):
    while not q.empty():
        first = q.get()
        for ii in adj[first]:
            if colors[ii] is None:
                colors[ii] = 1 - colors[first]
                q.put(ii)
            else:
                if colors[ii] == colors[first]:
                    return 0
    return 1


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
