n, k = map(int, input().split())
nums = list(map(int, input().split()))
result = -1000001

for i in range(n-k+1):
    result = max(sum(nums[i:i+k]), result)
print(result)