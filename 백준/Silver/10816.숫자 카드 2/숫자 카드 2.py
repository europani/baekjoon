from collections import Counter

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

counter = Counter(n_arr)

for b in m_arr:
    result = counter.get(b)
    print(result if result else 0, end=' ')