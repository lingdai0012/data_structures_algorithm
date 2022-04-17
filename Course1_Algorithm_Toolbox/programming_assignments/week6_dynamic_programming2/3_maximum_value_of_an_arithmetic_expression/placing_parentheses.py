# Uses python3
def evalt(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    # write your code here
    numbers = []
    symbols = []
    for ii in range(len(dataset)):
        if ii % 2 == 0:
            numbers.append(int(dataset[ii]))
        else:
            symbols.append(dataset[ii])

    def top_down_dp(numbers, symbols):
        if len(numbers) == 1:
            return numbers[0]
        max_result = 0
        for ii in range(len(symbols)):
            temp_result = top_down_dp(
                numbers[:ii]
                + [evalt(numbers[ii], numbers[ii + 1], symbols[ii])]
                + numbers[ii + 2 :],
                symbols[:ii] + symbols[ii + 1 :],
            )
            if temp_result > max_result:
                max_result = temp_result
        return max_result

    return top_down_dp(numbers, symbols)


if __name__ == "__main__":
    print(get_maximum_value(input()))
