def check(data):
    stack=[]

    for x in data:
        if x=='(':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                return
    if stack:
        print("NO")
    else:
        print("YES")

n = int(input())
for _ in range(n):
    data = list(map(str, input()))
    check(data)