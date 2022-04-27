n = int(input())
cnt=0
symbol='666'
now=666

while True:
    if symbol in str(now):
        cnt+=1
    if cnt==n:
        print(now)
        break
    now+=1