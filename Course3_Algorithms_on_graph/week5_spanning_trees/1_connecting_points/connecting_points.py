# Uses python3
import sys
import math
import heapq
from collections import namedtuple

point = namedtuple("point", ["x", "y"])


def mean_sqaure_distance(point_1, point_2):
    return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)


def minimum_distance(x, y):
    result = 0.0
    # write your code here
    points = [point(x[ii], y[ii]) for ii in range(len(x))]
    distances = [(math.inf, ii, None) for ii in range(len(x))]
    distances[0] = (0, 0, None)
    visited = [False for _ in range(len(x))]
    heaped_distances = distances.copy()
    heapq.heapify(heaped_distances)

    tree = []
    while len(heaped_distances) != 0:
        source_element = heapq.heappop(heaped_distances)
        if visited[source_element[1]]:
            continue
        visited[source_element[1]] = True
        tree.append((source_element[0], points[source_element[1]], source_element[2]))
        result += source_element[0]
        for ii in range(len(points)):
            if visited[ii]:
                continue
            temp_dist = mean_sqaure_distance(points[ii], points[source_element[1]])
            if temp_dist < distances[ii][0]:
                distances[ii] = (temp_dist, ii, source_element[1])
                heapq.heappush(heaped_distances, distances[ii])
    return round(result, 8)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
