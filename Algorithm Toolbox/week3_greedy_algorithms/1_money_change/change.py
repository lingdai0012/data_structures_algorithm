# Uses python3
import sys

def get_change(m):
    #write your code here
    number_coins = 0
    value = m
    for coin_value in [10, 5, 1]:
        number_temp = int(value/coin_value)
        if number_temp == 0:
            continue
        else:
            number_coins += number_temp
            value = value%coin_value
    return number_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
