def numSquares(n):
    dp = [0] + [float('inf')]*n
    print(dp)
    for i in range(1, n+1):
        dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
    return dp[n]

# https://leetcode.com/problems/perfect-squares/discuss/275311/Python-DP-and-BFS


print(numSquares(12))
