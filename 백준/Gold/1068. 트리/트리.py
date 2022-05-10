from collections import deque

n = int(input())
parent = list(map(int, input().split()))
target = int(input())
result=0

graph = [list() for _ in range(n)]

for c, p in enumerate(parent):
    if p>=0:
        graph[p].append(c)

def bfs(target):
    queue=deque([target])
    if parent[target]!=-1:
        graph[parent[target]].pop()

    while queue:
        now=queue.popleft()

        for i in graph[now]:
            queue.append(i)
        graph[now]=-1

bfs(target)

for x in graph:
    if x==[]:
        result+=1
print(result)