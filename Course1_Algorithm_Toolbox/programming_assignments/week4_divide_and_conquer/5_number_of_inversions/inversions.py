import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a, b, left, right, ave)
    return number_of_inversions


def merge(a, b, left, right, ave):
    number_of_inversions = 0
    left_list = a[left:ave].copy()
    right_list = a[ave:right].copy()
    i = 0
    j = 0
    k = left
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            a[k] = left_list[i]
            i += 1
        else:
            a[k] = right_list[j]
            number_of_inversions += left + len(left_list) + j - k
            j += 1
        k += 1

    while i < len(left_list):
        a[k] = left_list[i]
        k += 1
        i += 1

    while j < len(right_list):
        a[k] = right_list[j]
        k += 1
        j += 1
    return number_of_inversions


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
