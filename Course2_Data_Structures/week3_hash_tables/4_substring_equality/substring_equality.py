# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 10e9 + 7
        self.m2 = 10e9 + 9
        self.x = 1
        self.hashtable_1 = self.precompute(self.m1)
        self.hashtable_2 = self.precompute(self.m2)

    def precompute(self, m):
        hashtable = [0]
        for ii in range(len(self.s)):
            hashtable.append((self.x * hashtable[ii] + ord(self.s[ii])) % m)
        return hashtable

    def ask(self, a, b, l):
        hash_a_1 = self.hashtable_1[a + l] - self.x**l * self.hashtable_1[a]
        hash_b_1 = self.hashtable_1[b + l] - self.x**l * self.hashtable_1[b]
        hash_a_2 = self.hashtable_2[a + l] - self.x**l * self.hashtable_2[a]
        hash_b_2 = self.hashtable_2[b + l] - self.x**l * self.hashtable_2[b]
        if (
            hash_a_1 % self.m1 == hash_b_1 % self.m1
            and hash_a_2 % self.m2 == hash_b_2 % self.m2
        ):
            return s[a : a + l] == s[b : b + l]
        else:
            return False


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
