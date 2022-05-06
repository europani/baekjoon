n = int(input())
result=99

if n >= 1 and n <= 99:
    result=n
else:
    for i in range(100, n+1):
        nums = list(map(int, str(i)))
        if nums[2]-nums[1] == nums[1]-nums[0]:
            result+=1
print(result)