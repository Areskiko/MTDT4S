#list[list[float]]
def pp(frames) -> None:
    """
    Pretty print the memory frames.
    """

    print("-"*(len(frames[0])*5))
    for (i, frame) in enumerate(frames):
        print('Frame{}'.format(i), end='')
        for value in frame:
            value = value if value != None else 'X'
            print(' |{:>2}'.format(value), end='')
        print()
        print("-"*(len(frame)*5))


if __name__ == "__main__":
    f1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 4]
    f2 = [None, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    f3 = [None, None, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5]

    pp([f1, f2, f3])