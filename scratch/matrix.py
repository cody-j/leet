
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
            if (i,j) in seen:
                continue

            max_size = max(checkLocation(i, j), max_size)
            print('max: ', max_size)


if __name__=="__main__":
    ocean = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
    ]


    islands(ocean)
