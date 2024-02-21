def numSquares(n):
    # Initialize an array to store the least number of perfect square numbers for each value up to n
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 0 can be represented with 0 perfect squares

    # Iterate through each number up to n
    for i in range(1, n + 1):
        # Check for each perfect square less than or equal to i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

# Example usage:
print(numSquares(12))  # Output: 3
print(numSquares(13))  # Output: 2
