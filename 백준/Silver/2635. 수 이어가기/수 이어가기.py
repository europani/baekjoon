n = int(input())
arr=[]

for i in range(1, n+1):
    sub_arr=[n, i]
    
    while sub_arr[-2]-sub_arr[-1] >= 0:
        sub_arr.append(sub_arr[-2]-sub_arr[-1])

    if len(sub_arr) > len(arr):
        arr=sub_arr

print(len(arr))
print(*arr)