# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


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


def fibonacci_partial_sum_efficient(from_, to):
    last_digit_to = get_fibonacci_huge_efficient(to + 2, 10)
    last_digit_from = get_fibonacci_huge_efficient(from_ + 1, 10)
    if last_digit_to < last_digit_from:
        return 10 + last_digit_to - last_digit_from
    else:
        return last_digit_to - last_digit_from


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_efficient(from_, to))
