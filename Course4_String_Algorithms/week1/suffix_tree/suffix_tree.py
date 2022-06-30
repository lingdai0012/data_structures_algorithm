# python3
import sys
from collections import namedtuple


NODE_ID = 0
node = namedtuple("node", ["node_id", "pattern_end"])


def build_trie(text_patterns, text):
    global NODE_ID
    tree = dict()
    # write your code here
    root_node = node(0, None)
    for text_pattern in text_patterns:
        pattern = text[text_pattern:]
        curr_node = root_node
        for ii in range(len(pattern)):
            curr_symbol = pattern[ii]
            curr_node_next_edge = tree.get(curr_node, None)
            if curr_node_next_edge is not None:
                end_node = curr_node_next_edge.get(curr_symbol, None)
                if end_node is not None:
                    if ii == len(pattern) - 1:
                        updated_node = node(end_node.node_id, text_pattern)
                        curr_node_next_edge.update({curr_symbol: updated_node})
                        if end_node in tree:
                            tree[updated_node] = tree[end_node]
                            tree.pop(end_node)
                            end_node = updated_node
                    curr_node = end_node
                else:
                    NODE_ID += 1
                    new_node = node(
                        NODE_ID, text_pattern if ii == len(pattern) - 1 else None
                    )
                    curr_node_next_edge.update({curr_symbol: new_node})
                    curr_node = new_node
            else:
                NODE_ID += 1
                new_node = node(
                    NODE_ID, text_pattern if ii == len(pattern) - 1 else None
                )
                tree[curr_node] = {curr_symbol: new_node}
                curr_node = new_node
    return tree


def dfs(trie, key, value, edge, result):
    edge += key
·后缀树    if value not in trie:
        result.append(edge)
    elif len(trie[value]) == 1:
        dfs(
            trie,
            list(trie[value].items())[0][0],
            list(trie[value].items())[0][1],
            edge,
            result,
        )
    else:
        result.append(edge)
        for key, value in trie[value].items():
            dfs(
                trie,
                key,
                value,
                "",
                result,
            )
    return


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    text_patterns = [ii for ii in range(len(text))]
    suffix_trie = build_trie(text_patterns, text)
    starting_node = node(0, None)
    edge = ""
    dfs(suffix_trie, "", starting_node, edge, result)
    return result[1:]


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
