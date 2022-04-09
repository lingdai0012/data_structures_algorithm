def binary_search(keys, query):
    low = 0
    high = len(keys) - 1
    equals = []
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if keys[mid] == query:
            equals.append(mid)
            high = mid - 1
        elif keys[mid] > query:
            high = mid - 1
        else:
            low = mid + 1
    return min(equals) if len(equals) != 0 else -1


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")
