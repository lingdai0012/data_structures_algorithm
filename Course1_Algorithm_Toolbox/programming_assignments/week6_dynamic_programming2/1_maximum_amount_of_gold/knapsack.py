# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    results = [0]
    remaining_gold = [w]
    for capacity in range(1, W + 1):
        maximum_weight = 0
        usable_gold = w
        for gold in w:
            if capacity < gold:
                continue
            else:
                if gold in remaining_gold[capacity - gold]:
                    if gold + results[capacity - gold] > maximum_weight:
                        maximum_weight = max(
                            maximum_weight, gold + results[capacity - gold]
                        )
                        usable_gold = remaining_gold[capacity - gold].copy()
                        usable_gold.remove(gold)
                    else:
                        continue
                else:
                    if results[capacity - gold] > maximum_weight:
                        maximum_weight = max(maximum_weight, results[capacity - gold])
                        usable_gold = remaining_gold[capacity - gold]
                    else:
                        continue
        results.append(maximum_weight)
        remaining_gold.append(usable_gold)
    return results[-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
