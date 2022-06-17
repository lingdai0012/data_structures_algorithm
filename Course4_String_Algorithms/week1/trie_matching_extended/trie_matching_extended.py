# python3
import sys
from collections import namedtuple


NODE_ID = 0
node = namedtuple("node", ["node_id", "pattern_end"])


def build_trie(patterns):
    global NODE_ID
    tree = dict()
    # write your code here
    root_node = node(0, False)
    for pattern in patterns:
        curr_node = root_node
        for ii in range(len(pattern)):
            curr_symbol = pattern[ii]
            curr_node_next_edge = tree.get(curr_node, None)
            if curr_node_next_edge is not None:
                end_node = curr_node_next_edge.get(curr_symbol, None)
                if end_node is not None:
                    if ii == len(pattern) - 1:
                        updated_node = node(end_node.node_id, True)
                        curr_node_next_edge.update({curr_symbol: updated_node})
                        if end_node in tree:
                            tree[updated_node] = tree[end_node]
                            tree.pop(end_node)
                            end_node = updated_node
                    curr_node = end_node
                else:
                    NODE_ID += 1
                    new_node = node(NODE_ID, True if ii == len(pattern) - 1 else False)
                    curr_node_next_edge.update({curr_symbol: new_node})
                    curr_node = new_node
            else:
                NODE_ID += 1
                new_node = node(NODE_ID, True if ii == len(pattern) - 1 else False)
                tree[curr_node] = {curr_symbol: new_node}
                curr_node = new_node
    return tree


def prefix_matching(text, trie):
    ii = 0
    curr_node = node(0, False)
    path = ""
    while True:
        if curr_node not in trie or curr_node.pattern_end:
            return path
        elif ii >= len(text) or text[ii] not in trie[curr_node]:
            return None
        else:
            curr_node = trie[curr_node][text[ii]]
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
