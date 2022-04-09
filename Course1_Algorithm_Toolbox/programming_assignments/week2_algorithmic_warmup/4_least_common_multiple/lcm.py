# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd_efficient(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd_efficient(b, remainder)


def lcm_efficient(a, b):
    gcd = gcd_efficient(a, b)
    return int(a * b / gcd)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))
