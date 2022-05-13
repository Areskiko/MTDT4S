import math


def main():
    blocksize = int(input("Størrelse på en blokk: "))
    rowsize = int(input("Størrelse på en post: "))
    rowcount = int(input("Antall poster: "))
    keysize = int(input("Størrelse på søkenøkkel: "))
    pointersize = int(input("Størrelse på trepeker: "))

    rowperblock = math.floor(blocksize / rowsize * 2 / 3)
    print("Poster per blokk = ", rowperblock)
    innerrowperblock = math.floor(blocksize / (keysize + pointersize) * 2 / 3)
    print("Peker/nøkkel par per blokk = ", innerrowperblock)

    nodes = nodecount(rowcount, rowperblock)
    print("Antall løvnoder = ", nodes)
    
    count = 0

    while (nodes != 1):
        count += 1
        nodes = nodecount(nodes, innerrowperblock)
        print("Antall noder på nivå", count, "= ", nodes)

    input()


def nodecount(prevlayer, rowperblock):
    return math.ceil(prevlayer / rowperblock)


main()
