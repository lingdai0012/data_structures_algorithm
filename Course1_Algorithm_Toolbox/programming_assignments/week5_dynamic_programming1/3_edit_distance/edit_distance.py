# Uses python3
import numpy as np 

def edit_distance(s, t):
    #write your code here
    s_len = len(s)
    t_len = len(t)
    distances = np.zeros(shape = (s_len+1, t_len+1), dtype=int)
    for i in range(s_len + 1):
        distances[i, 0] = i
    for j in range(t_len + 1):
        distances[0, j] = j
    for j in range(1, t_len + 1):
        for i in range(1, s_len + 1):
            min_distance = min(distances[i-1, j]+1, distances[i, j-1]+1, distances[i-1, j-1]+1*int(s[i-1]!=t[j-1]))
            distances[i, j] = min_distance
    return distances[s_len, t_len]

if __name__ == "__main__":
    print(edit_distance(input(), input()))