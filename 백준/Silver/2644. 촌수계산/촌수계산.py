from collections import deque

n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [list() for _ in range(n+1)]
distance=[-1]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    queue = deque([s])
    distance[s]=0

    while queue:
        now = queue.popleft()

        if now == e:
            return

        for i in graph[now]:
            if distance[i] == -1:
                distance[i]=distance[now]+1
                queue.append(i)

bfs(s)
print(distance[e])