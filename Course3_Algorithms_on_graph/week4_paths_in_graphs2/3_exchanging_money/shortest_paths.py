# Uses python3

import sys
import queue
from collections import namedtuple

edge = namedtuple("edge", ["start", "end", "cost"])
max_weight = 10**19


def bellman_ford(distance, reachable, edges):
    updated_index = []
    for edge in edges:
        if (
            distance[edge.start] != max_weight
            and distance[edge.end] > distance[edge.start] + edge.cost
        ):
            distance[edge.end] = distance[edge.start] + edge.cost
            reachable[edge.end] = 1
            updated_index.append(edge.end)
    return updated_index


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    edges = [
        edge(ii, adj[ii][jj], cost[ii][jj])
        for ii in range(len(adj))
        for jj in range(len(adj[ii]))
    ]
    reachable[s] = 1
    distance[s] = 0
    for _ in range(len(adj) - 1):
        _updated_index = bellman_ford(distance, reachable, edges)
        if _updated_index == []:
            return

    queue = bellman_ford(distance, reachable, edges)
    visited = [False for _ in range(len(adj))]
    while len(queue) != 0:
        u = queue.pop(0)
        shortest[u] = 0
        visited[u] = True
        for v in adj[u]:
            if not visited[v] and v not in queue:
                queue.append(v)
    return


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
    s = data[0]
    s -= 1
    distance = [max_weight] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print("*")
        elif shortest[x] == 0:
            print("-")
        else:
            print(distance[x])
