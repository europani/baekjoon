import sys
from collections import deque
INF = sys.maxsize

a, b = map(int, input().split())
visited = [INF]*100001

def bfs(p):
    # init
    queue = deque([p])
    visited[p]=0

    while queue:
        now = queue.popleft()

        # 종료조건
        if now==b:
            return
    
        for x in [now-1, now+1, 2*now]:
            if 0<=x<=100000 and visited[x]==INF:
                visited[x]=visited[now]+1
                queue.append(x)

bfs(a)
print(visited[b])