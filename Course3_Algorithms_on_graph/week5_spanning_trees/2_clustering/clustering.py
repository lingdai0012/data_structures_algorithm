# Uses python3
import sys
import math
from collections import namedtuple
import heapq

point = namedtuple("point", ["x", "y"])
edge = namedtuple("edge", ["weight", "point1", "point2"])


def mean_sqaure_distance(point_1, point_2):
    return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)


def find(x, parents):
    if parents[x] == x:
        return x
    return find(parents[x], parents)


def union(x, y, parents):
    x_ancestor = find(x, parents)
    y_ancestor = find(y, parents)
    if x_ancestor <= y_ancestor:
        parents[y_ancestor] = x_ancestor
    else:
        parents[x_ancestor] = y_ancestor
    return parents


def clustering(x, y, k):
    # write your code here
    points = [point(x[ii], y[ii]) for ii in range(len(x))]
    edges = [
        edge(mean_sqaure_distance(points[ii], points[jj]), ii, jj)
        for ii in range(len(x))
        for jj in range(ii + 1, len(x))
    ]
    heapq.heapify(edges)
    used_edges = []
    parents = [_ for _ in range(len(points))]
    while len(edges) != 0:
        temp_edge = heapq.heappop(edges)
        if find(temp_edge.point1, parents) != find(temp_edge.point2, parents):
            parents = union(temp_edge.point1, temp_edge.point2, parents)
            used_edges.append(temp_edge)

    return round(used_edges[len(x) - k][0], 8)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0 : 2 * n : 2]
    y = data[1 : 2 * n : 2]
    data = data[2 * n :]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
