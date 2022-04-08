import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque([x])
    visited[x]=True

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        result+=1
print(result)