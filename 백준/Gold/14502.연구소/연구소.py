import copy
import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
zero_list = []
two_list = []
safe = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(comb_idx):
    copy_graph = copy.deepcopy(graph)
    queue = deque(two_list)

    for a, b in comb[comb_idx]:
        copy_graph[a][b]=1
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                queue.append((nx, ny))

    return copy_graph

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_list.append((i, j))
        elif graph[i][j] == 2:
            two_list.append((i, j))

comb = list(combinations(zero_list, 3))

for i in range(len(comb)):
    result = bfs(i)
    cnt = 0
    for x in result:
        cnt+=x.count(0)
    safe = max(cnt, safe)
print(safe)