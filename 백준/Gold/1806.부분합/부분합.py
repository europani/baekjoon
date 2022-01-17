N, S = map(int, input().split())
arr = list(map(int, input().split()))
shortest=100001

left=0
right=0
sub_sum=0

while True:
    leng = right-left

    if sub_sum >= S: 
        shortest=min(leng, shortest)
        sub_sum-=arr[left]
        left+=1
    elif right == N:
        break
    else:
        sub_sum+=arr[right]
        right+=1

if shortest != 100001:
    print(shortest)
else:
    print(0)