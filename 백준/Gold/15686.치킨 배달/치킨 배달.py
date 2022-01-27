from itertools import combinations
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i,j))

chicken_choise = list(combinations(chicken, C))
result = []

for choice in chicken_choise:
    distance = [INF] * len(house)
    for c in choice:
        for i, v in enumerate(house):
            distance[i] = min(abs(c[0]-v[0]) + abs(c[1]-v[1]), distance[i])
    result.append(sum(distance))
print(min(result))