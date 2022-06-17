# python3
import sys

NODE_ID = 0


def build_trie(patterns):
    global NODE_ID
    tree = dict()
    # write your code here
    for pattern in patterns:
        curr_node = 0
        for ii in range(len(pattern)):
            curr_symbol = pattern[ii]
            curr_node_next_edge = tree.get(curr_node, None)
            if curr_node_next_edge is not None:
                end_node = curr_node_next_edge.get(curr_symbol, None)
                if end_node is not None:
                    curr_node = end_node
                else:
                    NODE_ID += 1
                    curr_node_next_edge.update({curr_symbol: NODE_ID})
                    curr_node = NODE_ID
            else:
                NODE_ID += 1
                tree[curr_node] = {curr_symbol: NODE_ID}
                curr_node = NODE_ID
    return tree


def prefix_matching(text, trie):
    ii = 0
    node = 0
    path = ""
    while True:
        if node not in trie:
            return path
        elif ii >= len(text) or text[ii] not in trie[node]:
            return None
        else:
            node = trie[node][text[ii]]
            path += text[ii]
            ii += 1


def solve(text, n, patterns):
    result = []
    # write your code here
    trie = build_trie(patterns)
    for ii in range(len(text)):
        matched_pattern = prefix_matching(text[ii:], trie)
        if matched_pattern is not None:
            result.append(ii)
        else:
            continue
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(" ".join(map(str, ans)) + "\n")
