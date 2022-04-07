# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    sorted_index = sorted(list(range(len(weights))), reverse=True, key=lambda ii: values[ii]/weights[ii])
    for ii in sorted_index:
        if capacity >= weights[ii]:
            value += values[ii]
            capacity -= weights[ii]
        else:
            value += values[ii]*capacity/weights[ii]
            capacity = 0
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
