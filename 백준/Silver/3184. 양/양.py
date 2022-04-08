import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = [0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y]=True
    o, v = 0, 0

    while queue:
        cx, cy = queue.popleft()
        if graph[cx][cy]=='o':
          o+=1
        elif graph[cx][cy]=='v':
          v+=1

        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
  
            if graph[nx][ny]!='#' and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny]=True

    if o>v:
        result[0]+=o
    else:
        result[1]+=v

for i in range(n):
    for j in range(m):
        if graph[i][j] in ['v', 'o'] and not visited[i][j]:
            bfs(i, j)
print(*result)