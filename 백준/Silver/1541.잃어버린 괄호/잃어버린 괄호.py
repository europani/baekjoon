inp = input().split('-')
result = 10000

for x in inp:
    sub_sum = sum(map(int, x.split('+')))
    if result==10000:
        result=sub_sum
    else:
        result-=sub_sum
print(result)
