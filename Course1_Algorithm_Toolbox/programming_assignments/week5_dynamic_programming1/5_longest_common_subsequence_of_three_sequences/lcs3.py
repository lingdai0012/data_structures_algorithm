#Uses python3

import sys
import numpy as np

def lcs3(a, b, c):
    #write your code here
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)
    longest_subsequence_num = np.zeros(shape=(a_len+1, b_len+1, c_len+1), dtype=int)
    for ii in range(1, a_len+1):
        for jj in range(1, b_len+1):
            for kk in range(1, c_len+1):
                if a[ii-1] == b[jj-1] == c[kk-1]:
                    longest_subsequence_num[ii, jj, kk] = min(max(longest_subsequence_num[ii-1, jj, kk]+1, 
                                                      longest_subsequence_num[ii, jj-1, kk]+1,
                                                      longest_subsequence_num[ii, jj, kk-1]+1), 
                                                  min(ii, jj, kk))
                else:
                    longest_subsequence_num[ii, jj, kk] = max(longest_subsequence_num[ii-1, jj, kk]+1, 
                                                      longest_subsequence_num[ii, jj-1, kk]+1,
                                                      longest_subsequence_num[ii, jj, kk-1]+1)                
    return longest_subsequence_num[a_len, b_len, c_len]

if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
