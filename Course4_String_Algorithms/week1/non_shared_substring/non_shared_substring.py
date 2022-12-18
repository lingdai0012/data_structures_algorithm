# python3
import sys
from collections import namedtuple
sys.setrecursionlimit(10**6)

class SuffixTree:
    class Node:
        def __init__(self, start: int = None, end: int = None):
            self.start = start
            self.end = end
            self.state = None
            self.children = {}

    def __init__(self, text):
        self.text = text
        self.text_len = len(text)
        self.root = self.Node()
        self.build_tree()
        self.min_unique_string = self.text

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

    def update_state(self, node: Node):
        if len(node.children) == 0:
            if "#" in self.text[node.start:node.end]:
                node.state = "L"
            else:
                node.state = "R"
        else:
            states = set()
            for _, child in node.children.items():
                child_state = self.update_state(child)
                states.add(child_state)
            if "M" in states or len(states) > 1:
                node.state = "M"
            else:
                node.state = states.pop()
        return node.state


    def find_min_non_shared_string(self, node: Node, stored: str):
        for _, child in node.children.items():          
            if child.state != "M":
                if self.text[child.start] in ("#", "$")  or child.state == "R":
                    continue
                else:
                    temp_min_unique_string =  stored + self.text[child.start]
                    if len(self.min_unique_string) > len(temp_min_unique_string):
                        self.min_unique_string = temp_min_unique_string
                    else:
                        continue
            else:
                self.find_min_non_shared_string(child, stored + self.text[child.start:child.end])
        return


def solve(p, q):
    text = p + "#" + q + "$"
    sf = SuffixTree(text)
    sf.update_state(sf.root)
    sf.find_min_non_shared_string(sf.root, "")
    return sf.min_unique_string

if __name__ == "__main__":
    p = sys.stdin.readline().strip()
    q = sys.stdin.readline().strip()

    ans = solve(p, q)

    sys.stdout.write(ans + "\n")









