# Uses python3
import sys

# def get_majority_element(a, left, right):
#     count = {}
#     for num in a:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
#     max_freq = max(count.values())
#     if max_freq > len(a)/2:
#         return 1 
#     else:
#         return -1

def get_majority_element(a, left, right):
    mid = (left + right)//2 
    if len(a[left:right])==1:
        return a[left]
    if len(a[left:right])==2:
        return a[left] if a[left]==a[left+1] else -1
    left_majority_element = get_majority_element(a, left, mid)
    right_majority_element = get_majority_element(a, mid, right)
    majority = compare_majorities(left_majority_element, right_majority_element, a, left, mid, right)
    return majority

def compare_majorities(left_majority_element, right_majority_element, a, left, mid, right):
    if left_majority_element == -1 and right_majority_element == -1:
        return -1
    elif left_majority_element == right_majority_element:
        return left_majority_element
    elif left_majority_element == -1:
        if sum([num==right_majority_element for num in a[left:right]]) > len(a[left:right])/2:
            return right_majority_element
        else:
            return -1
    elif right_majority_element == -1:
        if sum([num==left_majority_element for num in a[left:right]]) > len(a[left:right])/2:
            return left_majority_element
        else:
            return -1  
    else:
        left_weight = 0
        right_weight = 0
        for num in a[left:right]:
            if num == left_majority_element:
                left_weight += 1
            if num == right_majority_element:
                right_weight += 1           

        if left_weight > len(a[left:right])/2:
            return left_majority_element
        elif right_weight > len(a[left:right])/2:
            return right_majority_element
        else:
            return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
