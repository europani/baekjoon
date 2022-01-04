from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
result = list(combinations_with_replacement(nums, m))

for x in result:
    print(" ".join(map(str, x)))