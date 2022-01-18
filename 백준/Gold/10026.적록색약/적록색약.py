import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]
ans1, ans2 = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue

        if graph[nx][ny] == color:
            if not visited[nx][ny]:
                dfs(nx, ny)

def change_color():
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='G':
                graph[i][j]='R'


visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans1+=1
            dfs(i, j)

change_color()

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans2+=1
            dfs(i, j)
print(ans1, ans2)