from enum import Enum
class Split(Enum):
    LEFT = 1
    RIGHT = 2

def gen_tree(in_list, split_opt, slots):
    """Generate a B-tree from a list of elements"""
    if len(in_list) == 0:
        return None
    if len(in_list) == 1:
        return in_list[0]
    if split_opt == Split.LEFT:
        return gen_tree(in_list[:len(in_list)//2], split_opt, slots)
    elif split_opt == Split.RIGHT:
        return gen_tree(in_list[len(in_list)//2:], split_opt, slots)
    else:
        raise ValueError("Invalid split option")
    
if __name__ == "__main__":
    elems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    tree = gen_tree(elems, Split.LEFT, 4)
    print(tree)