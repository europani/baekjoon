import sys
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        day = graph[x][y]
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            
            if graph[nx][ny]==0:
                graph[nx][ny]=day+1
                queue.append((nx, ny))

bfs()

for x in graph:
    if 0 in x:
        print(-1)
        sys.exit(0)

print(max(map(max, graph))-1)