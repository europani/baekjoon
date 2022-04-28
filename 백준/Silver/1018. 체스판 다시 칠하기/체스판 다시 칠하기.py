n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
result = n*m    

def check_board(x, y, graph, color):
    global result
    cnt=0
  
    for i in range(x, x+8):
        for j in range(y, y+8):            
            distance = abs(i-x) + abs(j-y)

            if distance%2==0 and graph[i][j]!=color:
                cnt+=1
            elif distance%2!=0 and graph[i][j]==color:
                cnt+=1

            # BackTracking
            if cnt >= result:
                return
  
    if cnt < result:
        result=cnt

for i in range(n-7):
    for j in range(m-7):
        check_board(i, j, graph, 'B')
        check_board(i, j, graph, 'W')
print(result)