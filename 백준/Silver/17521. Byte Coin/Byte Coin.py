n, m = map(int, input().split())
price = [int(input()) for _ in range(n)]

min_p, max_p = price[0], price[0]
stock=0    # 보유 코인수

for i in range(n-1):
    if price[i] <= price[i+1]:
        if not stock:
            stock+=m//min_p
            m-=min_p*stock
        max_p = price[i+1]
    else:
        if stock:
            m+=stock*max_p
            stock=0
        min_p = price[i+1]

if stock:
    m+=stock*max_p
print(m)