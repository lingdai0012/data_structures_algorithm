#Uses python3

import sys
import itertools

def create_first_digit_map(a):
    mapper = {}
    for x in a:
        if x[0] not in mapper:
            mapper[x[0]] = [x]
        else:
            mapper[x[0]].append(x)
    return mapper


def get_best_permutation_same_first_digit(numbers):
    # first_digit = numbers[0][0]
    # longest_number= max(numbers, key=lambda x: len(x))
    # longest_length = len(longest_number)
    # padded_numbers = [number + longest_number[:longest_length-len(number)] if longest_length > len(number) else number for number in numbers ]
    # sorted_padded_numbers_index = sorted(list(range(len(padded_numbers))), reverse=True, key=lambda x: int(padded_numbers[x]))
    largest_number_combination = []
    for number in numbers:
        if largest_number_combination == []:
            largest_number_combination.append(number)
            largest_number = int(number)
        else:
            temp_largest_number = 0
            temp_largest_combination = []
            for i in range(len(largest_number_combination)+1):
                temp_combination = largest_number_combination[:i] + [number] + largest_number_combination[i:]
                if int("".join(temp_combination)) > temp_largest_number:
                    temp_largest_number = int("".join(temp_combination))
                    temp_largest_combination = temp_combination
            largest_number_combination = temp_largest_combination
    return "".join(largest_number_combination)


def largest_number(a):
    #write your code here
    res = ""
    a_mapper = create_first_digit_map(a)
    sorted_a_mapper = dict(sorted(a_mapper.items(), reverse=True, key=lambda x: int(x[0])))
    sorted_sorted_a_mapper = {key:get_best_permutation_same_first_digit(value)  for key, value in sorted_a_mapper.items()}
    for key, value in sorted_sorted_a_mapper.items():
        res += sorted_sorted_a_mapper[key]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
