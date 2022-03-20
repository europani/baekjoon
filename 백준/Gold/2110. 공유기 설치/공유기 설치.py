# 답안확인
n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))

left = 0
right = max(houses)-min(houses)
answer = -1

while left <= right:
    mid = (left+right)//2

    cnt=1
    last = houses[0]
    for i in range(1, n):
        if houses[i]-last < mid:
            continue
        cnt+=1
        last = houses[i]

    if cnt >= c:
        answer = mid
        left=mid+1
    else:
        right=mid-1
        
print(answer)   