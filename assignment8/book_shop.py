import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    x = int(data[1])
    h = list(map(int, data[2:n+2]))    # prices
    s = list(map(int, data[n+2:]))     # pages

    dp = [0] * (x + 1)

    for i in range(n):
        price = h[i]
        pages = s[i]
        for j in range(x, price - 1, -1):  # backwards to avoid reuse
            dp[j] = max(dp[j], dp[j - price] + pages)

    print(max(dp))

main()
