import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [list() for _ in range(v+1)]
distance = [-1] * (v+1)
result=0

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    global result
    queue = deque([start])
    distance[start]=0

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if distance[i]==-1:
                distance[i]=distance[now]+1
                result+=1
                if distance[i] < 2:
                    queue.append(i)
bfs(1)
print(result)