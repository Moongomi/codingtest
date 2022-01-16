import sys
input = sys.stdin.readline

n,k = map(int, input().split())
dp = [0]*(100002)
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp[0] = 1
for i in range(1,n+1):
    for j in range(coins[i-1],k+1):
        dp[j] += dp[j-coins[i-1]]
print(dp[k])

