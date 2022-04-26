# 답안확인
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
max_num = max(map(max, graph))
result=0

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, level, total):
    global result
    # Base Case
    if level == 4:
        result=max(total, result)
        return

    # Backtracking
    if total+max_num*(4-level) < result:
        return 

    for i in range(4):
        nx, ny = x+d[i][0], y+d[i][1]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visited[nx][ny]:
            if level==2:    # shape ㅗ
                visited[nx][ny]=True
                dfs(x, y, level+1, total+graph[nx][ny])
                visited[nx][ny]=False
        
            visited[nx][ny]=True
            dfs(nx, ny, level+1, total+graph[nx][ny])
            visited[nx][ny]=False

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i, j, 1, graph[i][j])
        visited[i][j]=False

print(result)    