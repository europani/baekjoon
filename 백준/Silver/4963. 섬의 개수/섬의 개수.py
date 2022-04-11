import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(init_x, init_y, graph, a, b):
    queue = deque()
    queue.append((init_x, init_y))
    graph[init_x][init_y]='0'

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= b or ny >= a:
                continue

            if graph[nx][ny]=='1':
                graph[nx][ny]='0'
                queue.append((nx, ny))


while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    
    graph = [list(input().split()) for _ in range(b)]
    result = 0

    for i in range(b):
        for j in range(a):
            if graph[i][j]=='1':
                bfs(i, j, graph, a, b)
                result+=1

    print(result)