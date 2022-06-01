from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0]=True

    while queue:
        x, y = queue.popleft()
        dist = graph[x][y]     

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            if graph[nx][ny] != 0 and not visited[nx][ny]:    
                graph[nx][ny]=dist+1
                visited[nx][ny]=True
                queue.append((nx, ny))

bfs()
print(graph[n-1][m-1])