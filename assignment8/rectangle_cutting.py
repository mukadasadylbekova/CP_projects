def min_moves_to_cut(a, b):
    dp = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == j:
                dp[i][j] = 0
            else:
                res = float('inf')
                for k in range(1, i):
                    res = min(res, dp[k][j] + dp[i - k][j])
                for k in range(1, j):
                    res = min(res, dp[i][k] + dp[i][j - k])
                dp[i][j] = res + 1
    return dp[a][b]

# Input
a, b = map(int, input().split())
print(min_moves_to_cut(a, b))

