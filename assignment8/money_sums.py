n = int(input())
coins = list(map(int, input().split()))

MAX_SUM = sum(coins)
dp = [False] * (MAX_SUM + 1)
dp[0] = True

for coin in coins:
    for i in range(MAX_SUM, coin - 1, -1):
        if dp[i - coin]:
            dp[i] = True


result = [i for i in range(1, MAX_SUM + 1) if dp[i]]


print(len(result))
print(' '.join(map(str, result)))
