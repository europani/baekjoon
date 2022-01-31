import copy
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cleaner = []
dust = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    if graph[i][0] == -1:
        cleaner.append(i)

def diff():
    after = [[0] * m for _ in range(n)]

    for i in cleaner:
        after[i][0] = -1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] not in (-1, 0):
                after[i][j] += graph[i][j]

                for a in range(4):
                    nx = i + dx[a]
                    ny = j + dy[a]

                    if nx>=n or ny>=m or nx<0 or ny<0:
                        continue
                    
                    if graph[nx][ny]!=-1:
                        after[i][j] -= graph[i][j]//5
                        after[nx][ny] += graph[i][j]//5
    return after


def clean(graph):
    after = copy.deepcopy(graph)
    u, d = cleaner

    # upper
    for i in range(m-1, 1, -1):
        after[u][i] = graph[u][i-1]
    after[u][1]=0
    for i in range(u-1, -1, -1):
        after[i][m-1] = graph[i+1][m-1]
    for i in range(m-1):
        after[0][i] = graph[0][i+1]
    for i in range(1, u):
        after[i][0] = graph[i-1][0]

    # lower
    for i in range(m-1, 1, -1):
        after[d][i] = graph[d][i-1]
    after[d][1]=0
    for i in range(d+1, n):
        after[i][m-1] = graph[i-1][m-1]
    for i in range(m-1):
        after[n-1][i] = graph[n-1][i+1]
    for i in range(d+1, n-1):
        after[i][0] = graph[i+1][0]

    return after
    
for _ in range(t):
    after = diff()
    graph = clean(after)
    dust = sum(map(sum, graph))+2
print(dust)