n = int(input())
nums = list(map(int, input().split()))
target = int(input())
result = 0

nums.sort()
left = 0
right = n-1

while left < right:
    if nums[left] + nums[right] == target:
        result+=1
        left+=1
    elif nums[left] + nums[right] > target:
        right-=1
    else:
        left+=1
print(result)