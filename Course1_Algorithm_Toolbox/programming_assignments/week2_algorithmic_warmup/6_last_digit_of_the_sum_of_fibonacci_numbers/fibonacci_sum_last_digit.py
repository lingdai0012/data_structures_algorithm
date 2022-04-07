# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def get_fibonacci_huge_efficient(n, m):
    fib = []
    fib.extend([0, 1])
    period = None
    for _ in range(2, n+1):
        fib.append((fib[_-1] + fib[_-2]) % m)
        if (fib[_] == 0) and (fib[_] + fib[_-1]==1):
            period = _
            break

    if period is None:
        return fib[n]
    else:
        return fib[n%period]


def fibonacci_sum_efficient(n):
    if get_fibonacci_huge_efficient(n+2, 10) < 1:
        return 9 + get_fibonacci_huge_efficient(n+2, 10)
    return get_fibonacci_huge_efficient(n+2, 10)-1



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_efficient(n))
