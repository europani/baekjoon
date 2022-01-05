n = int(input())
time = list(map(int, input().split()))
time.sort()

sum = 0
l_sum = 0

for t in time:
    l_sum+=t
    sum+=l_sum
print(sum)