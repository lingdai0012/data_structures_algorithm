# python3
import sys
from collections import namedtuple
sys.setrecursionlimit(10**6)

class SuffixTree:
    class Node:
        def __init__(self, start: int = None, end: int = None):
            self.start = start
            self.end = end
            self.children = {}

    def __init__(self, text):
        self.text = text
        self.text_len = len(text)
        self.root = self.Node()
        self.build_tree()

    def build_tree(self):
        init_node = self.Node(0, self.text_len)
        self.root.children[self.text[0]] = init_node    
        for ii in range(1, self.text_len):
            node = self.root.children.get(self.text[ii], None)
            if node is None:
                self.root.children[self.text[ii]] = self.Node(ii, self.text_len)
            else:
                self.break_node(node, ii)


    def break_node(self, node: Node, text_start: int):
        node_edge_length = node.end - node.start
        new_edge_length = self.text_len - text_start
        min_length = min(node_edge_length, new_edge_length)
        for ii in range(min_length):
            if self.text[node.start + ii] == self.text[text_start + ii]:
                if ii == min_length - 1:
                    if node_edge_length<new_edge_length:
                        next_node = node.children.get(self.text[text_start + min_length], None)
                        if next_node is None:
                            node.children.update({self.text[text_start + min_length]: self.Node(text_start + min_length, self.text_len)})
                            break
                        else:
                            self.break_node(next_node, text_start + min_length)
                continue
            else:
                extended_node = self.Node(node.start + ii, node.end)
                new_node = self.Node(text_start + ii, self.text_len)
                while len(node.children) > 0:
                    label, kid = node.children.popitem()
                    extended_node.children.update({label:kid})
                node.end = node.start + ii
                node.children.update({self.text[node.start + ii]: extended_node})
                node.children.update({self.text[text_start + ii]: new_node})
                break

    def collect_result(self, node:Node, result:list) -> None:
        for _, next_node in node.children.items():
            result.append(self.text[next_node.start:next_node.end])
            self.collect_result(next_node, result)


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    st = SuffixTree(text) 
    st.collect_result(st.root, result)
    return result


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))




