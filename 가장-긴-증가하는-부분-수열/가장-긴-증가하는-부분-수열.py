n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i-1, -1, -1):      
        if nums[j] < nums[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))