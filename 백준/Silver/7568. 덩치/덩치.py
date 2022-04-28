n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

for height, weight in people:
    cnt=0
    for h, w in people:
        if height < h and weight < w:
            cnt+=1
    print(cnt+1, end=' ')