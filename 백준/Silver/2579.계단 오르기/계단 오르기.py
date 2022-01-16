import sys
input = sys.stdin.readline

n = int(input())
point = [int(input()) for _ in range(n)]
point.insert(0, 0)
dp = [0] * (n+1)
dp[1] = point[1]

for i in range(2, n+1):
    if i==2:
        dp[i] = dp[i-1] + point[i]
    else:
        dp[i] = max(dp[i-2], dp[i-3]+point[i-1])+point[i]

print(dp[n])