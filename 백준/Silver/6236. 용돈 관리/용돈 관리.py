n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

left = max(money)
right = 1000000000
answer = -1

while left <= right:
    mid = (left+right)//2
    
    cnt, remain = 0, 0
    for x in money:
        if remain < x:
            cnt+=1
            remain=mid-x
        else:
            remain-=x

    if cnt > m:
        left = mid+1
    else:
        answer = mid
        right = mid-1
print(answer)    