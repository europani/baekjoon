h = int(input())
arr = [''] + input().split()
i = 2**(h-1)

while i > 0:
    for j in range(i, 2**h+1, i*2):
        print(arr[j], end=' ')
    i//=2
    print()