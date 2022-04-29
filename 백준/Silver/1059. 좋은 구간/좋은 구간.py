l = int(input())
s = [0]+sorted(map(int, input().split()))
n = int(input())

min, max = 0, 0

# Search
for i in range(len(s)-1):
    if s[i] < n and n < s[i+1]:
        min, max = s[i], s[i+1]
        break

result = (n-min)*(max-n)
print(0 if result<=0 else result-1)