# 답안확인
import sys
sys.setrecursionlimit(10**5)
nums=[]

while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break

def post_order(left, right):
    if left > right:
        return
      
    mid=right+1
    for i in range(left+1, right+1):
        if nums[i] > nums[left]:
            mid=i
            break

    post_order(left+1, mid-1)
    post_order(mid, right)
    print(nums[left])

post_order(0, len(nums)-1)