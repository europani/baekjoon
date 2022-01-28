from itertools import permutations

n, r = map(int, input().split())
nums = sorted(list(map(int, input().split())))

perms = sorted(set(permutations(nums, r)))
for perm in perms:
    print(*perm)