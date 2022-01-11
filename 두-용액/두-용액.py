import sys
max=sys.maxsize

n = int(input())
liq = list(map(int, input().split()))
liq.sort()

left=0
right=len(liq)-1
gap=max
l, r = left, right

while left < right:
    sum = liq[left]+liq[right]
    if gap > abs(sum):
        gap=abs(sum)
        l, r = left, right
    
    if sum > 0:
        right-=1
    else:
        left+=1

print(liq[l], liq[r])