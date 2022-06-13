# Uses python3

import sys
import math
import heapq
import logging
from collections import namedtuple


dist_element = namedtuple("dist_element", ["distance", "index"])


def distance(adj, cost, s, t):
    # write your code here
    dist = [
        dist_element(0, _)
        if _ == s
        else dist_element(cost[s][adj[s].index(_)], _)
        if _ in adj[s]
        else dist_element(math.inf, _)
        for _ in range(len(adj))
    ]
    heap_dist = dist.copy()
    prev = [None for _ in range(len(adj))]
    visited = [False for _ in range(len(adj))]
    heapq.heapify(heap_dist)
    while len(heap_dist) > 0:
        min_distance_element = heapq.heappop(heap_dist)
        if visited[min_distance_element.index]:
            continue
        visited[min_distance_element.index] = True
        for ii in range(len(adj[min_distance_element.index])):
            if (
                dist[adj[min_distance_element.index][ii]].distance
                > dist[min_distance_element.index].distance
                + cost[min_distance_element.index][ii]
            ):
                smaller_element = dist_element(
                    dist[min_distance_element.index].distance
                    + cost[min_distance_element.index][ii],
                    adj[min_distance_element.index][ii],
                )
                prev[adj[min_distance_element.index][ii]] = min_distance_element.index
                dist[adj[min_distance_element.index][ii]] = smaller_element
                heapq.heappush(heap_dist, smaller_element)
    return dist[t].distance if dist[t].distance != math.inf else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
