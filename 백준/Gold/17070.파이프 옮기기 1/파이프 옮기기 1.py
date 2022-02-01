n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

dx = [0, 1, 1]
dy = [1, 1, 0]

# flag 1:horizonal, 2:diagonal, 3:vertical
def dfs(x, y, flag):
    global result
    if x == n-1 and y == n-1:
        result+=1
        return

    if flag in (1, 2):
        if y+1 < n and graph[x][y+1] == 0:
            dfs(x, y+1, 1)
    if flag in (2, 3):
        if x+1 < n and graph[x+1][y] == 0:
            dfs(x+1, y, 3)
    if x+1 < n and y+1 < n:
        if graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] ==0:
            dfs(x+1, y+1, 2)

dfs(0, 1, 1)
print(result)