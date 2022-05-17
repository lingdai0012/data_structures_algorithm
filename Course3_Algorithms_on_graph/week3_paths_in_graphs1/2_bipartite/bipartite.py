# Uses python3

import sys
import queue


def bipartite(adj):
    # write your code here
    used = [0 for _ in range(len(adj))]
    colors = [None for _ in range(len(adj))]
    q = queue.Queue()
    q.put(0)
    colors[0] = 0
    return bfs(adj, q, used, colors)


def bfs(adj, q, used, colors):
    while not q.empty():
        first = q.get()
        for ii in adj[first]:
            if used[ii] == 0:
                colors[ii] = 1 - colors[first]
                used[ii] = 1
                q.put(ii)
            else:
                if colors[ii] != 1 - colors[first]:
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
