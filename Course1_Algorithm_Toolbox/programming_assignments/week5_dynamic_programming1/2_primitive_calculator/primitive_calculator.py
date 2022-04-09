# Uses python3
import sys
import math


def optimal_sequence(n):
    min_num_operations = [0, 0]
    optimal_sequences = [[], [1]]
    for i in range(2, n + 1):
        num_operations_3 = min_num_operations[i // 3] + 1 if i % 3 == 0 else math.inf
        num_operations_2 = min_num_operations[i // 2] + 1 if i % 2 == 0 else math.inf
        num_operations_1 = min_num_operations[i - 1] + 1
        possible_numbers = [num_operations_3, num_operations_2, num_operations_1]
        next_to_add = [
            optimal_sequences[i // 3],
            optimal_sequences[i // 2],
            optimal_sequences[i - 1],
        ]
        min_number = min(possible_numbers)
        next_sequence = next_to_add[possible_numbers.index(min_number)] + [i]
        min_num_operations.append(min_number)
        optimal_sequences.append(next_sequence)
    return optimal_sequences[n]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")
