from itertools import combinations_with_replacement

n, r = map(int, input().split())
nums = sorted(list(map(int, input().split())))

perms = list(combinations_with_replacement(nums, r))
for perm in perms:
    print(*perm)