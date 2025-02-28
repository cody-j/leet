
def islands(ocean):
    """
    Returns an integer with the largest island size
    """
    seen = set()
    max_size = 0

    def checkLocation(i,j):
        if (i,j) in seen:
            return 0

        seen.add((i,j))

        if i >= len(ocean) or j >= len(ocean[0]) or i < 0 or j < 0:
            return 0

        if ocean[i][j] == 0:
            return 0

        size = 1
        for [n,m] in [(1,0), (-1,0), (0,1), (0,-1)]:
            size += checkLocation(i+n, j+m)

        return size


    for i in range(len(ocean)):
        for j in range(len(ocean[0])):
            max_size = max(checkLocation(i, j), max_size)

    return max_size


def wordsearch(letters, word):
    directions = [(1,0),(1,1),(0,1),(-1, 0),(0,-1),(-1,-1),(-1,1),(1,-1)]

    def search(i,j, dir, subword):
        if len(subword) == 0:
            return 1

        try:
            letter = letters[i][j]
        except IndexError:
            return 0

        if letter != subword[0]:
            return 0

        return search(i+dir[0], j+dir[1], dir, subword[1:])

    appearances = 0

    for i in range(len(letters)):
        for j in range(len(letters[0])):
            for dir in directions:
                appearances += search(i, j, dir, word)

    return appearances

if __name__=="__main__":
    ocean = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
    ]

    letters = [
        ['A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'C', 'A'],
        ['A', 'A', 'A', 'A', 'A'],
        ['A', 'T', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A'],
    ]

    # print(islands(ocean))
    print(wordsearch(letters, 'CAT'))
