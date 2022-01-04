def check(i):
    for j in range(i):
        if queen[i] == queen[j] or queen[i]-i == queen[j]-j or queen[i]+i == queen[j]+j:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result+=1
        return

    for i in range(n):
        queen[x]=i
        if check(x):
            dfs(x+1)

n = int(input())
result = 0
queen = [-1] * n

dfs(0)
print(result)
