m, n = map(int, input().split())
nums = [True] * (n+1)
nums[0], nums[1] = False, False

for i in range(2, n+1):
    if nums[i] == True:
        for j in range(i*2, n+1, i):
            nums[j]=False

for i in range(m, n+1):
    if nums[i]==True:
        print(i)