n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards.sort()

def binary_search(target, start, end):
    if start > end:
        return 0

    mid = (start+end)//2
    if cards[mid]==target:
        return 1
    elif cards[mid] > target:
        return binary_search(target, start, mid-1)
    else:
        return binary_search(target, mid+1, end)

for x in nums:
    print(binary_search(x, 0, n-1), end=' ')