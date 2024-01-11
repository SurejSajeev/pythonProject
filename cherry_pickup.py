def cherryPickup(grid):
    n = len(grid)
    dp = [[float('-inf')] * n for _ in range(n)]

    dp[0][0] = grid[0][0]

    #To reach the bottom-right corner from the top-left corner,
    # you need to move n - 1 steps to the right and n - 1 steps down.
    # That's a total of 2 * (n - 1) steps.
    for t in range(1, 2 * n - 1):
        dp_next = [[float('-inf')] * n for _ in range(n)]

        for i in range(max(0, t - n + 1), min(n, t + 1)):
            for j in range(max(0, t - n + 1), min(n, t + 1)):
                if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                    continue

                cherries = grid[i][t - i]
                if i != j:
                    cherries += grid[j][t - j]

                dp_next[i][j] = max(
                    dp_next[i][j],
                    cherries + max(
                        dp[pre_i][pre_j] for pre_i in [i - 1, i] for pre_j in [j - 1, j] if pre_i >= 0 and pre_j >= 0)
                )

        dp = dp_next

    return max(0, dp[n - 1][n - 1])


# Example usage:
grid1 = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
print(cherryPickup(grid1))  # Output: 5

grid2 = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
print(cherryPickup(grid2))  # Output: 0

# """[[0,1,-1],
#     [1,0,-1],
#     [1,1,1]]""""