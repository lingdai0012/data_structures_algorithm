# python3

import sys
from collections import namedtuple

Answer = namedtuple("answer_type", "i j len")


class hash:
    def __init__(self, s, x, m):
        self.x = x
        self.m = m
        self.s = s
        self.hash_table = self.get_hash_sum()

    def get_hash_sum(self):
        n = len(self.s)
        h = [0]
        for ii in range(1, n + 1):
            val = (self.x * h[ii - 1] % self.m + ord(self.s[ii - 1]) % self.m) % self.m
            h.append(val)
        return h

    def get_hash(self, start, length):
        return (
            self.hash_table[start + length] % self.m
            - (pow(self.x, length, self.m) * self.hash_table[start] % self.m) % self.m
        )

    def get_hash_fixed_length(self, length):
        return [
            self.get_hash(ii, length) % self.m for ii in range(len(self.s) + 1 - length)
        ]


def check(hash_s1, hash_t1, hash_s2, hash_t2, start_l, end_l):
    l = (start_l + end_l) // 2
    hash_s1_l = hash_s1.get_hash_fixed_length(l)
    hash_s2_l = hash_s2.get_hash_fixed_length(l)
    hash_t1_l = hash_t1.get_hash_fixed_length(l)
    hash_t2_l = hash_t2.get_hash_fixed_length(l)

    possbile_max = Answer(0, 0, 0)
    for ii in range(len(hash_s1_l)):
        for jj in range(len(hash_t1_l)):
            if (hash_s1_l[ii] == hash_t1_l[jj]) and (hash_s2_l[ii] == hash_t2_l[jj]):
                temp_max = check_equality(
                    hash_s1,
                    hash_t1,
                    hash_s2,
                    hash_t2,
                    l,
                    min(len(hash_s1.s) + 1 - ii, len(hash_t1.s) + 1 - jj),
                    ii,
                    jj,
                )
                if temp_max.len > possbile_max.len:
                    possbile_max = temp_max
    if possbile_max.len > 0:
        return possbile_max
    elif possbile_max.len == 0 and end_l - start_l == 1:
        return Answer(0, 0, 0)
    else:
        return check(hash_s1, hash_t1, hash_s2, hash_t2, start_l, l)


def check_equality(
    hash_s1, hash_t1, hash_s2, hash_t2, start_l, end_l, s_index, t_index
):
    if end_l - start_l == 1:
        return Answer(s_index, t_index, start_l)
    l = (start_l + end_l) // 2
    if (
        hash_s1.get_hash(s_index, l) % hash_s1.m
        == hash_t1.get_hash(t_index, l) % hash_t1.m
        and hash_s2.get_hash(s_index, l) % hash_s2.m
        == hash_t2.get_hash(t_index, l) % hash_t2.m
    ):
        return check_equality(
            hash_s1, hash_t1, hash_s2, hash_t2, l, end_l, s_index, t_index
        )
    else:
        return check_equality(
            hash_s1, hash_t1, hash_s2, hash_t2, start_l, l, s_index, t_index
        )


def solve(s, t):
    m1 = 1000000000039
    m2 = 1000000000061

    x = 35
    hash_s1 = hash(s, x, m1)
    hash_s2 = hash(s, x, m2)

    hash_t1 = hash(t, x, m1)
    hash_t2 = hash(t, x, m2)

    start_l = 0
    end_l = min(len(hash_s1.s) + 1, len(hash_t1.s) + 1)
    return check(hash_s1, hash_t1, hash_s2, hash_t2, start_l, end_l)


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
