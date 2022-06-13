# Uses python3

import sys
import math
import random
from collections import namedtuple


edge = namedtuple("edge", ["start", "end", "cost"])
max_weight = 10**9


def bellman_ford(dist, prev, edges):
    relaxed = False
    for edge in edges:
        if (
            dist[edge.start] != max_weight
            and dist[edge.end] > dist[edge.start] + edge.cost
        ):
            dist[edge.end] = dist[edge.start] + edge.cost
            prev[edge.end] = edge.start
            relaxed = True
    return dist, prev, relaxed


def negative_cycle(adj, cost):
    # write your code here
    adj.append([_ for _ in range(len(adj))])
    cost.append([0 for _ in range(len(adj))])
    s = len(adj) - 1
    edges = [
        edge(ii, adj[ii][jj], cost[ii][jj])
        for ii in range(len(adj))
        for jj in range(len(adj[ii]))
    ]
    dist = [0 if _ == s else max_weight for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    for _ in range(len(adj) - 1):
        dist, prev, relaxed = bellman_ford(dist, prev, edges)
        if not relaxed:
            return 0

    dist_last, prev_last, relaxed_last = bellman_ford(dist, prev, edges)
    if relaxed_last:
        return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
