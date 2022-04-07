# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    last_stop = 0
    number_refill = 0
    stops.append(distance)
    for ii in range(len(stops)-1):
        if (stops[ii+1] - stops[ii]) > tank:
            return -1
        if (stops[ii] - last_stop) >= tank or (stops[ii+1] - last_stop) > tank:
            number_refill += 1
            last_stop = stops[ii]
        else:
            continue
    return number_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
