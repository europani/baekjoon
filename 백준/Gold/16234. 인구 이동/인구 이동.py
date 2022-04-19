import copy
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, s, e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
days=0

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def moving(arr, graph):
    total=sum(graph[x][y] for x, y in arr)

    for x, y in arr:
        graph[x][y]=total//len(arr)
    

def dfs(x, y, arr, visited):
    visited[x][y]=True
    arr+=[[x, y]]

    for i in range(4):
        nx, ny = x+d[i][0], y+d[i][1]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
          
        if s <= abs(graph[nx][ny]-graph[x][y]) <= e:
            if not visited[nx][ny]:
                dfs(nx, ny, arr, visited)

while True:
    new_graph = copy.deepcopy(graph)
    visited = [[False]*n for _ in range(n)] 
    flag=0
  
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                arr = []
                dfs(i, j, arr, visited)

                if len(arr) > 1:
                    moving(arr, new_graph)
                    flag=1

    if not flag:
        print(days)
        break

    graph=new_graph
    days+=1