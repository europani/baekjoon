# 답안확인
import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [list() for _ in range(n+1)]
v, d = 0, 0

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(x, sum):
    global v, d
    visited[x]=True

    if sum > d:
        v, d = x, sum

    for now, cost in graph[x]:
        if not visited[now]:
            dfs(now, sum+cost)

visited = [False] * (n+1)
dfs(1, 0)
visited = [False] * (n+1)
dfs(v, 0)
print(d)
