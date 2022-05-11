# 답안확인
n = int(input())
top = list(map(int, input().split()))
result = [0] * n
stack=[]

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            result[i]=stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append((i, top[i]))

print(*result)