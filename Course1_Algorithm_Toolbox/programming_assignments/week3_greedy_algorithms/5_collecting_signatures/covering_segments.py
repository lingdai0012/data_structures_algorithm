# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def check_is_covered(s, covered_list):
    if len(covered_list) == 0:
        return True
    for ele in covered_list:
        if s.start >  ele.end:
            return False
    return True

def optimal_points(segments):
    points = []
    #write your code here
    sorted_segments = sorted(segments, key=lambda s: s.start)
    covered_list = []
    for ii in range(len(sorted_segments)):
        s = sorted_segments[ii]
        is_covered = check_is_covered(s, covered_list)
        if is_covered is True:
            covered_list.append(s)
            if ii == len(sorted_segments)-1:
                points.append(min(covered_list, key=lambda s: s.end).end)
            else:
                continue
        else:
            points.append(min(covered_list, key=lambda s: s.end).end)
            covered_list = [s]
            if ii == len(sorted_segments)-1:
                points.append(min(covered_list, key=lambda s: s.end).end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
