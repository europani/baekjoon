from collections import deque
n = int(input())

def check(func, arr, reversed):
    for fun in func:
        if fun=='R':
            reversed=True if reversed==False else False
        else:
            if arr:
                if reversed:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return -1
    if reversed:
        arr.reverse()

    return arr


for _ in range(n):
    func = list(input())
    arr_n = int(input())
    reversed = False

    arr=deque(input().replace('[', '').replace(']', '').split(','))

    if arr_n < func.count('D'):
        print('error')
        continue

    result = check(func, arr, reversed)

    if result != -1:
        print('['+','.join(list(result))+']')