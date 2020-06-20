def minPathSum(grid):
    h, w = len(grid), len(grid[0])
    dp_table = grid

    for x in range(1, w):
        dp_table[0][x] = grid[0][x] + dp_table[0][x-1]

    for y in range(1, h):
        dp_table[y][0] = grid[y][0] + dp_table[y-1][0]

    for y in range(1, h):
        for x in range(1, w):
            dp_table[y][x] = grid[y][x] + \
                min(dp_table[y][x-1], dp_table[y-1][x])

    return dp_table[h-1][w-1]

# https://leetcode.com/problems/minimum-path-sum/submissions/
