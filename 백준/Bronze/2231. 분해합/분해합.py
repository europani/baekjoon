n = int(input())

for i in range(1, n):
    answer= i+sum(map(int, list(str(i))))
    if answer==n:
        print(i)
        break
else:
    print(0)