n = int(input())
dic = dict()

def pre_order(x):
    if x!='.':
        print(x, end='')
        pre_order(dic[x][0])
        pre_order(dic[x][1])

def in_order(x):
    if x!='.':
        in_order(dic[x][0])
        print(x, end='')
        in_order(dic[x][1])

def post_order(x):
    if x!='.':
        post_order(dic[x][0])
        post_order(dic[x][1])
        print(x, end='')

for _ in range(n):
    r, a, b = input().split()
    dic[r]=[a, b]

pre_order('A')
print()
in_order('A')
print()
post_order('A')