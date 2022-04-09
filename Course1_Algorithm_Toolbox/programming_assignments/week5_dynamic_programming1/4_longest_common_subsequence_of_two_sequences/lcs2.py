# Uses python3

import sys
import numpy as np


def lcs2(a, b):
    # write your code here
    a_len = len(a)
    b_len = len(b)
    number_commom_sequences = np.zeros(shape=(a_len + 1, b_len + 1), dtype=int)
    for ii in range(1, a_len + 1):
        for jj in range(1, b_len + 1):
            if a[ii - 1] == b[jj - 1]:
                number_commom_sequences[ii, jj] = max(
                    number_commom_sequences[ii - 1, jj] + 1,
                    number_commom_sequences[ii, jj - 1] + 1,
                    number_commom_sequences[ii - 1, jj - 1] + 1,
                )
            else:
                number_commom_sequences[ii, jj] = max(
                    number_commom_sequences[ii - 1, jj],
                    number_commom_sequences[ii, jj - 1],
                    number_commom_sequences[ii - 1, jj - 1],
                )
    return number_commom_sequences[a_len, b_len]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
