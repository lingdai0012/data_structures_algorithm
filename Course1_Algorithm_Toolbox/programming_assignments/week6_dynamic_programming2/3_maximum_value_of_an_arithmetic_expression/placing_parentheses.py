# Uses python3
import numpy as np
import math


def evalt(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        assert False


# def get_maximum_value(dataset):
#     # write your code here
#     numbers = []
#     symbols = []
#     for ii in range(len(dataset)):
#         if ii % 2 == 0:
#             numbers.append(int(dataset[ii]))
#         else:
#             symbols.append(dataset[ii])

#     def top_down_dp(numbers, symbols):
#         if len(numbers) == 1:
#             return numbers[0]
#         max_result = 0
#         for ii in range(len(symbols)):
#             temp_result = top_down_dp(
#                 numbers[:ii]
#                 + [evalt(numbers[ii], numbers[ii + 1], symbols[ii])]
#                 + numbers[ii + 2 :],
#                 symbols[:ii] + symbols[ii + 1 :],
#             )
#             if temp_result > max_result:
#                 max_result = temp_result
#         return max_result

#     return top_down_dp(numbers, symbols)


def get_maximum_value(dataset):

    numbers = []
    symbols = []
    for ii in range(len(dataset)):
        if ii % 2 == 0:
            numbers.append(int(dataset[ii]))
        else:
            symbols.append(dataset[ii])

    M = np.zeros(shape=(len(numbers), len(numbers)), dtype=int)
    m = np.zeros(shape=(len(numbers), len(numbers)), dtype=int)
    for ii in range(len(numbers)):
        M[ii, ii] = numbers[ii]
        m[ii, ii] = numbers[ii]
        if ii < len(numbers) - 1:
            M[ii, ii + 1] = evalt(numbers[ii], numbers[ii + 1], symbols[ii])
            m[ii, ii + 1] = evalt(numbers[ii], numbers[ii + 1], symbols[ii])
    for jj in range(2, len(numbers)):
        for ii in range(jj - 1, -1, -1):
            max_val = -math.inf
            min_val = math.inf
            for k in range(ii, jj):
                possible_results = [
                    evalt(m[ii, k], m[k + 1, jj], symbols[k]),
                    evalt(M[ii, k], M[k + 1, jj], symbols[k]),
                    evalt(M[ii, k], m[k + 1, jj], symbols[k]),
                    evalt(m[ii, k], M[k + 1, jj], symbols[k]),
                ]
                if max(possible_results) > max_val:
                    max_val = max(possible_results)
                if min(possible_results) < min_val:
                    min_val = min(possible_results)
            M[ii, jj] = max_val
            m[ii, jj] = min_val
    return M[0, -1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
