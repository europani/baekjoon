def binary_search(array, target, start, end, max_idx):
    if start > end:
        return max_idx

    mid = (start+end)//2
    if array[mid] < target:
        max_idx = max(mid, max_idx)
        return binary_search(array, target, mid+1, end, max_idx)
    else:
        return binary_search(array, target, start, mid-1, max_idx)
    

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = sorted(map(int, input().split()))

    result = 0
    for x in arr_a:
        idx = binary_search(arr_b, x, 0, b-1, -1)
        if idx>-1:
            result += (idx+1)
    print(result)        