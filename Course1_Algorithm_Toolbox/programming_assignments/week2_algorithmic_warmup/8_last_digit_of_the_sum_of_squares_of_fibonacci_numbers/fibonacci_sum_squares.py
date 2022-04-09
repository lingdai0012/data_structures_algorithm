# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def get_fibonacci_huge_efficient(n, m):
    fib = []
    fib.extend([0, 1])
    period = None
    for _ in range(2, n + 1):
        fib.append((fib[_ - 1] + fib[_ - 2]) % m)
        if (fib[_] == 0) and (fib[_] + fib[_ - 1] == 1):
            period = _
            break

    if period is None:
        return fib[n]
    else:
        return fib[n % period]


def fibonacci_sum_squares_efficient(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (
        get_fibonacci_huge_efficient(n, 10)
        * (
            get_fibonacci_huge_efficient(n, 10)
            + get_fibonacci_huge_efficient(n - 1, 10)
        )
        % 10
    )


if __name__ == "__main__":
    n = int(stdin.read())
    print(fibonacci_sum_squares_efficient(n))
