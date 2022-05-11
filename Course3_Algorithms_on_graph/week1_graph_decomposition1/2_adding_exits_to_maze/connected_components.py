# Uses python3

import sys


def number_of_components(adj):
    result = 0
    # write your code here
    for ii in range(len(adj)):
        if adj[ii] is not None:
            result += 1
            traverse(adj, ii)
        else:
            continue
    return result


def traverse(adj, ii):
    if adj[ii] is None:
        return
    else:
        adjacents = adj[ii]
        adj[ii] = None
        for vertice in adjacents:
            traverse(adj, vertice)
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
    print(number_of_components(adj))
