import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    dp = [1] * (m+1)
    
    for i in range(3, m):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[m-1])
    