MOD = 10**9 + 7

def solve():
    
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    
   
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    
    if x[0] == 0:
        for v in range(1, m + 1):
            dp[1][v] = 1
    else:
        dp[1][x[0]] = 1
    
    
    for i in range(1, n):
        if x[i] == 0:
           
            for v in range(1, m + 1):
                if v > 1:
                    dp[i + 1][v] += dp[i][v - 1]
                dp[i + 1][v] += dp[i][v]
                if v < m:
                    dp[i + 1][v] += dp[i][v + 1]
                dp[i + 1][v] %= MOD
        else:
           
            v = x[i]
            if v > 1:
                dp[i + 1][v] += dp[i][v - 1]
            dp[i + 1][v] += dp[i][v]
            if v < m:
                dp[i + 1][v] += dp[i][v + 1]
            dp[i + 1][v] %= MOD

   
    result = sum(dp[n][v] for v in range(1, m + 1)) % MOD
    print(result)

solve()
