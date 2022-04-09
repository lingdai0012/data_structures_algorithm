# Uses python3
def calc_fib(n):
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


n = int(input())
print(calc_fib(n))
