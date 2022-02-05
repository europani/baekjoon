import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while True:
    # clean
    if graph[x][y] ==0:
        result+=1
        graph[x][y]=2   # visit
    
    # search
    cnt=0
    while True:
        if graph[x+dx[d]][y+dy[d]]==0:    # left side
            x+=dx[d]
            y+=dy[d]
            d = d-1 if d!=0 else 3
            break
        else:
            if cnt < 4:
                d = d-1 if d!=0 else 3
                cnt+=1
            else:
                tmp = d-1 if d!=0 else 3
                if graph[x+dx[tmp]][y+dy[tmp]] != 1:
                    x += dx[tmp]
                    y += dy[tmp]
                    cnt=0
                else:
                    print(result)
                    sys.exit() 