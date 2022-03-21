n, t = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
sub_sum = nums[0]
answer = 0

while True:
    if sub_sum == t:
        answer+=1
    
    if sub_sum >= t:
        sub_sum-=nums[left]
        left+=1
    else:
        right+=1
        if right == n:
            break
        sub_sum+=nums[right]
print(answer)