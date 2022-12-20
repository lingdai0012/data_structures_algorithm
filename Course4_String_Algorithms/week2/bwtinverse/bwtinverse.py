# python3
import sys
import time

def InverseBWT(bwt):
    # write your code here
    bwt_list, sorted_bwt_list, target = add_label(bwt)
    last_to_first_map = {bwt_list[ii]:sorted_bwt_list[ii] for ii in range(len(bwt_list))}
    original_text = []
    while True:
        original_text.append(bwt[target])
        target = last_to_first_map[target]
        if bwt[target] == "$":
            break
    return "".join(original_text[1:] + original_text[:1])

def add_label(bwt: str) -> tuple:
    occurrence = {}
    element_dict = {"$": [], "A":[], "C":[], "G":[], "T":[]}
    bwt_list= []
    target_index = None
    for ii in range(len(bwt)):
        char = bwt[ii]
        if char == "$":
            target_index = ii
        occurrence[char] = occurrence.get(char, 0) + 1
        bwt_list.append(ii)
        element_dict[char].append(ii)
    sorted_bwt_list = element_dict["$"] + element_dict["A"] + element_dict["C"] + element_dict["G"] + element_dict["T"]
    return bwt_list, sorted_bwt_list, target_index


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
    