def max_pairwise_product(numbers):
    n = len(numbers)
    max_1 = 0
    for i in range(1, n):
        if numbers[i] > max_1:
            max_1 = numbers[i]
    numbers.remove(max_1)
    max_2 = 0
    for j in range(n - 1):
        if numbers[j] > max_2:
            max_2 = numbers[j]
    max_product = max_1 * max_2
    return max_product


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
