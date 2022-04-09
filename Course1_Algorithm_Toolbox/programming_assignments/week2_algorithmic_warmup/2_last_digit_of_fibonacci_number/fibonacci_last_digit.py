# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    fib = list(range(n + 1))
    fib[0] = 0
    fib[1] = 1
    for _ in range(2, n + 1):
        fib[_] = (fib[_ - 1] + fib[_ - 2]) % 10

    return fib[n]


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
