# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    all_points = starts + points + ends
    sorted_all_points_index = sorted(
        list(range(len(all_points))),
        key=lambda ii: (
            starts[ii]
            if ii < len(starts)
            else ends[ii - len(starts) - len(points)]
            if ii >= len(starts) + len(points)
            else points[ii - len(starts)],
            ii,
        ),
    )
    count_starts = 0
    count_ends = 0
    for ii in sorted_all_points_index:
        if ii < len(starts):
            count_starts += 1
        elif ii >= len(starts) + len(points):
            count_ends += 1
        else:
            cnt[ii - len(starts)] = count_starts - count_ends
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2]
    ends = data[3 : 2 * n + 2 : 2]
    points = data[2 * n + 2 :]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=" ")
