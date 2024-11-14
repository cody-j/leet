def min_path_sum(grid):
    # define dimensions m rows, n columns
    m, n = len(grid), len(grid[0])
    # define matrix of m, n dimensions
    dp = [[0]*n for _ in range(m)]

    # set top left of matrix to initial value
    dp[0][0] = grid[0][0]

    # set top row from left
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i-1]

    # set left column from above
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i-1][0]

    # calculate inner as min from top or left + value in grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(
                dp[i-1][j],
                dp[i][j-1]
            ) + grid[i][j]

    return dp[m-1][n-1]

if __name__=="__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    print(min_path_sum(grid))
