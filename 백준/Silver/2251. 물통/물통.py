from collections import deque

A, B, C = map(int, input().split())
visited = [[False]*(B+1) for _ in range(A+1)]
result = []

def bfs():
    def pour(a, b):
        if not visited[a][b]:
            visited[a][b]=True
            queue.append((a, b))

    # 초기화
    queue = deque()
    queue.append((0, 0))
    visited[0][0]=True

    while queue:
        a, b = queue.popleft()
        c = C-a-b

        # 정답 추가
        if a==0:
            result.append(c)

        if a!=0:
            # A->B
            water = min(B-b, a)
            pour(a-water, b+water)

            # A->C
            water = min(C-c, a)
            pour(a-water, b)

        if b!=0:
            # B->A
            water = min(A-a, b)
            pour(a+water, b-water)
        
            # B->C
            water = min(C-c, b)
            pour(a, b-water)

        if c!=0:
            # C->A
            water = min(A-a, c)
            pour(a+water, b)

            # C->B
            water = min(B-b, c)
            pour(a, b+water)

bfs()
print(' '.join(map(str, sorted(result))))