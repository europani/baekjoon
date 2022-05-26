from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

for pers in permutations(nums, m):
  for x in pers:
    print(x, end=' ')
  print()

