from math import ceil

# Compute the minimum block accesses needed to join two tables

def min_blocks(tab1_size, tab2_size, slots):
    """Compute the minimum number of blocks needed to join two tables"""

    mi = min(tab1_size, tab2_size)
    ma = max(tab1_size, tab2_size)

    rounds = ceil(mi/(slots-2))
    iter_per_round = ma

    return mi + rounds * iter_per_round

if __name__ == "__main__":
    t1 = int(input("Table 1 blocks: "))
    t2 = int(input("Table 2 blocks: "))
    sl = int(input("Memory blocks: "))
    print("Minimum blocks:", min_blocks(t1, t2, sl))
    input()