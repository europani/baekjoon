n = int(input())
drink = [0] + list(int(input()) for _ in range(n))
dp = [0] * (n+1)
dp[1]=drink[1]

for i in range(2, n+1):
    if i==2:
        dp[i]=drink[i-1]+drink[i]
    else:
        dp[i]=max(dp[i-3]+drink[i-1]+drink[i], dp[i-2]+drink[i], dp[i-1])
print(max(dp))