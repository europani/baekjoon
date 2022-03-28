n = int(input())
village = [list(input()) for _ in range(n)]
cnt = 0
cnt_arr = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
  global cnt
  if x>=n or y>=n or x<0 or y<0:
    return False
  
  if village[x][y] == '1':
    cnt+=1
    village[x][y]='0'

    for i in range(4):
      dfs(x+dx[i], y+dy[i])
    
    return True
  else:
    return False

for i in range(n):
  for j in range(n):
      result = dfs(i, j)
      if result:
        cnt_arr.append(cnt)
        cnt=0


print(len(cnt_arr))
for x in sorted(cnt_arr):
  print(x)

