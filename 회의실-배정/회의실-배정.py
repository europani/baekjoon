n = int(input())
com = [list(map(int, input().split())) for _ in range(n)]
com.sort(key=lambda x:(x[1], x[0]))

time = 0
cnt = 0

for s, e in com:
    if s >= time:
        time=e
        cnt+=1

print(cnt)