from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if visited[i] != True:
            dfs(graph, i, visited)

            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

v, n, start = map(int, input().split())
graph = [ [] for _ in range(v+1)]

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

visited = [False] * (v+1)    
dfs(graph, start, visited)
print()
visited = [False] * (v+1)    
bfs(graph, start, visited)
    