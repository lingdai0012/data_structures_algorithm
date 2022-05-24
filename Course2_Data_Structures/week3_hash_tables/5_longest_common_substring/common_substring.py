# python3

import sys
from collections import namedtuple

Answer = namedtuple("answer_type", "i j len")


def get_hash_sum(string, x, m):
    n = len(string)
    h = [0]
    for i in range(1, n + 1):
        val = (x * h[i - 1] % m + ord(string[i - 1]) % m) % m
        h.append(val)
    return h


def get_hash(hash_table, start, length, x, m):
    return (
        hash_table[start + length] % m - (pow(x, length, m) * hash_table[start] % m) % m
    )


def get_hash_k(hash_table, string, length, x, m):
    return [
        get_hash(hash_table, ii, length, x, m) for ii in range(len(string) + 1 - length)
    ]


def check_equality(
    ii,
    jj,
    start,
    end,
    hash_table_s_1,
    hash_table_t_2,
    hash_table_s_2,
    hash_table_t_1,
    x,
    m1,
    m2,
):
    if start == end or start == end - 1:
        return Answer(ii, jj, start)
    if ii + (start + end) // 2 >= len(hash_table_s_1) or jj + (start + end) // 2 >= len(
        hash_table_t_1
    ):
        return Answer(ii, jj, start)
    new_hash_s_k_1 = get_hash(hash_table_s_1, ii, (start + end) // 2, x, m1)
    new_hash_t_k_1 = get_hash(hash_table_t_1, jj, (start + end) // 2, x, m1)

    new_hash_s_k_2 = get_hash(hash_table_s_2, ii, (start + end) // 2, x, m2)
    new_hash_t_k_2 = get_hash(hash_table_t_2, jj, (start + end) // 2, x, m2)

    if (
        new_hash_s_k_1 % m1 == new_hash_t_k_1 % m1
        and new_hash_s_k_2 % m2 == new_hash_t_k_2 % m2
    ):
        return check_equality(
            ii,
            jj,
            (start + end) // 2,
            end,
            hash_table_s_1,
            hash_table_t_1,
            hash_table_s_2,
            hash_table_t_2,
            x,
            m1,
            m2,
        )
    else:
        return check_equality(
            ii,
            jj,
            start,
            (start + end) // 2,
            hash_table_s_1,
            hash_table_t_2,
            hash_table_s_2,
            hash_table_t_2,
            x,
            m1,
            m2,
        )


def solve(s, t):
    m1 = pow(10, 9) + 7
    m2 = pow(10, 9) + 9

    x = 1

    hash_table_s_1 = get_hash_sum(s, x, m1)
    hash_table_t_1 = get_hash_sum(t, x, m1)

    hash_table_s_2 = get_hash_sum(s, x, m2)
    hash_table_t_2 = get_hash_sum(t, x, m2)

    max_length = min([len(s), len(t)])
    middle = max_length // 2

    hash_table_s_middle_1 = get_hash_k(hash_table_s_1, s, middle, x, m1)
    hash_table_t_middle_1 = get_hash_k(hash_table_t_1, t, middle, x, m1)

    hash_table_s_middle_2 = get_hash_k(hash_table_s_2, s, middle, x, m2)
    hash_table_t_middle_2 = get_hash_k(hash_table_t_2, t, middle, x, m2)

    possible_equals = []
    for ii in range(len(hash_table_s_middle_1)):
        if hash_table_s_middle_1[ii] in hash_table_t_middle_1:
            jj = hash_table_t_middle_1.index(hash_table_s_middle_1[ii])
            if hash_table_s_middle_2[ii] % m2 == hash_table_t_middle_2[jj] % m2:
                possible_equals.append(
                    check_equality(
                        ii,
                        jj,
                        middle,
                        max_length,
                        hash_table_s_1,
                        hash_table_t_1,
                        hash_table_s_2,
                        hash_table_t_2,
                        x,
                        m1,
                        m2,
                    )
                )
    if len(possible_equals) == 0:
        return Answer(0, 1, 0)
    else:
        return max(possible_equals, key=lambda x: x[-1])


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
