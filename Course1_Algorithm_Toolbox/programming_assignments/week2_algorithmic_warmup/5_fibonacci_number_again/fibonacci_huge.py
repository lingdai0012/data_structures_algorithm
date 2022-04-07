# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


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

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_efficient(n, m))
