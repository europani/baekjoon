from collections import deque
import sys
INF = sys.maxsize

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
distance = [[[INF]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    distance[x][y][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=n or ny>=m or nx<0 or ny<0:
                continue

            if graph[nx][ny] == 0:
                if distance[nx][ny][0] == INF and distance[x][y][0] != INF:
                    distance[nx][ny][0]=distance[x][y][0]+1
                    queue.append((nx, ny))
                if distance[nx][ny][1] == INF:
                    distance[nx][ny][1]=distance[x][y][1]+1
                    queue.append((nx, ny))
            else:
                if distance[nx][ny][1] == INF and distance[x][y][0] != INF:
                    distance[nx][ny][1]=distance[x][y][0]+1
                    queue.append((nx, ny))


bfs(0, 0)
if distance[n-1][m-1] == [INF, INF]:
    print(-1)
else:
    print(min(distance[n-1][m-1])+1)
