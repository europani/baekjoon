import sys
from collections import deque
input = sys.stdin.readline

d = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

def bfs(sx, sy, ex, ey, distance):
    queue = deque()
    queue.append((sx, sy))
    distance[sx][sy]=0

    while queue:
        x, y = queue.popleft()

        if [x, y] == [ex, ey]:
            return distance[x][y]

        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if distance[nx][ny] == -1:
                distance[nx][ny]=distance[x][y]+1
                queue.append((nx, ny))

t = int(input())

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    distance = [[-1]*n for _ in range(n)]

    print(bfs(sx, sy, ex, ey, distance))
    