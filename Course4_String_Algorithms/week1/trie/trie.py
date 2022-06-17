# Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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


if __name__ == "__main__":
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
