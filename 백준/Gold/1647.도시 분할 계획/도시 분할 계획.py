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

v, e = map(int, input().split())
queue = []
parent = [0] * (v+1)
result = 0

for i in range(1, v+1):
    parent[i]=i

for _ in range(e):
    a, b, cost = map(int, input().split())
    queue.append((cost, a, b))

queue.sort()

for x in queue:
    cost, a, b = x

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
        last=cost

print(result-last)