# Uses python3
import sys
import math

def get_change(m):
    #write your code here
    min_num_coins = [math.inf]*(m+1)
    min_num_coins[0] = 0
    for i in range(1, m+1):
        for coin in [1, 3, 4]:
            if i >= coin:
                num_coins = min_num_coins[i-coin] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    return min_num_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
