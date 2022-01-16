n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort()

def binary_search(target, start, end):
    if start > end:
        return

    mid = (start+end)//2

    if n_arr[mid]==target:
        return True
    elif n_arr[mid]>target:
        return binary_search(target, start, mid-1)
    else:
        return binary_search(target, mid+1, end)

for b in m_arr:
    result = binary_search(b, 0, n-1)
    if result:
        print(1)
    else:
        print(0)
