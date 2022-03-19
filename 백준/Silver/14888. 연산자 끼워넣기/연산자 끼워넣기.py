import sys

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

maximum = -sys.maxsize
minimum = sys.maxsize

def cal(num1, num2, oper):
    if oper==0:
        return num1+num2
    elif oper==1:
        return num1-num2
    elif oper==2:
        return num1*num2
    else:
        if num1 < 0:
            return -(-num1//num2)
        else:
            return num1//num2

def dfs(idx, num):
    global maximum, minimum
    # Base Case
    if idx == n:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return

    for i in range(4):
        if opers[i]!=0:
            opers[i]-=1
            dfs(idx+1, cal(num, nums[idx], i))
            opers[i]+=1
                 
dfs(1, nums[0])
print(maximum, minimum, sep='\n')