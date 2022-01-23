def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a]=b
    else:
        parent[b]=a


n = int(input())
p = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
parent = [0] * n

for i in range(1, n):
    parent[i]=i

edges = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            edges.append((i,j))

for a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

dest = list(map(int, input().split()))

for i in range(len(dest)-1):
    if parent[dest[i]-1] != parent[dest[i+1]-1]:
        print("NO")
        break
else:
    print("YES")