# python3
import sys

def BWT(text):
    cyc_mat = cyclic_matrix(text)
    cyc_mat = sorted(cyc_mat)
    return "".join([row[-1] for row in cyc_mat])

def cyclic_matrix(text: str) -> list:
    return [text[ii:] + text[:ii] for ii in range(len(text))]



if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))