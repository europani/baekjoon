import sys
from collections import deque

n, m, k, s = map(int, input().split())
graph = [list() for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(s):
    queue = deque([s])
    distance[s]=0

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if distance[i] == -1:
                distance[i]=distance[now]+1
                queue.append(i)         
  
bfs(s)
flag=0
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        flag=1
if not flag:
    print(-1)