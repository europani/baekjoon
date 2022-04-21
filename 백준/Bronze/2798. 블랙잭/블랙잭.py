n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer=0

def dfs(idx, cnt, total):
    global answer
    # Base Case
    if cnt==3:
        if total <= m and answer < total:
            answer=total
        return

    for i in range(idx+1, n):
        dfs(i, cnt+1, total+cards[i])

dfs(0, 0, 0)
print(answer)