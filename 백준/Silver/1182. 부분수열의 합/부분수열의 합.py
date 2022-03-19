n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = 0

def dfs(idx, sum):
    global result
    if sum == s:
        result+=1

    for i in range(idx, n):
        dfs(i+1, sum+nums[i])

dfs(0, 0)
print(result if s != 0 else result-1)