# Uses python3
import sys
import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def filter_points_by_midline(x, y, midline, minimum_splitted_distance):
    index = list(range(len(x)))
    filtered_index = list(
        filter(lambda ii: abs(x[ii] - midline) <= minimum_splitted_distance, index)
    )
    filtered_x = [x[ii] for ii in filtered_index]
    filtered_y = [y[ii] for ii in filtered_index]
    return filtered_x, filtered_y


def half_search(x, y):
    if len(x) == 1:
        return math.inf
    if len(x) == 2:
        return calculate_distance(x[0], y[0], x[1], y[1])
    mid = len(x) // 2
    midline = (x[mid] + x[mid - 1]) / 2
    min_distance_left = half_search(x[:mid], y[:mid])
    min_distance_right = half_search(x[mid:], y[mid:])
    min_spiltted_distance = min(min_distance_left, min_distance_right)
    filtered_x, filtered_y = filter_points_by_midline(
        x, y, midline, min_spiltted_distance
    )
    filtered_index = list(range(len(filtered_x)))
    sorted_filltered_index = sorted(filtered_index, key=lambda ii: filtered_y[ii])
    sorted_filltered_x = [filtered_x[ii] for ii in sorted_filltered_index]
    sorted_filltered_y = [filtered_y[ii] for ii in sorted_filltered_index]
    minimum_strip_distance = math.inf
    for ii in range(len(sorted_filltered_y)):
        for jj in range(ii + 1, ii + 7):
            if jj >= len(sorted_filltered_y):
                break
            temp_distance = calculate_distance(
                sorted_filltered_x[ii],
                sorted_filltered_y[ii],
                sorted_filltered_x[jj],
                sorted_filltered_y[jj],
            )
            if temp_distance < minimum_strip_distance:
                minimum_strip_distance = temp_distance
    return min(minimum_strip_distance, min_spiltted_distance)


def minimum_distance(x, y):
    # write your code here
    index = list(range(len(x)))
    sorted_index = sorted(index, key=lambda ii: x[ii])
    sorted_x = [x[ii] for ii in sorted_index]
    sorted_y = [y[ii] for ii in sorted_index]
    minimum_splitted_distance = half_search(sorted_x, sorted_y)

    return minimum_splitted_distance


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
