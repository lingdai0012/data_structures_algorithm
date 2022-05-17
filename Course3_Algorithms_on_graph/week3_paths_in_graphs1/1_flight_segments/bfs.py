# Uses python3

import sys
import queue
import math


def distance(adj, s, t):
    # write your code here
    used = [0 for _ in range(len(adj))]
    q = queue.Queue()
    q.put((s, 0))
    min_distances = []
    used[s] = 1
    bfs(adj, q, t, min_distances, used)
    if min_distances == []:
        return -1
    else:
        return min(min_distances)


def bfs(adj, q, t, min_distances, used):
    while not q.empty():
        first, distance = q.get()
        for ii in adj[first]:
            if ii == t:
                min_distances.append(distance + 1)
            if used[ii] != 1:
                q.put((ii, distance + 1))
                used[ii] = 1
    return


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
