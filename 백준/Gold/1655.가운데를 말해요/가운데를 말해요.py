import heapq
import sys
input=sys.stdin.readline

n = int(input())
max_h = []
min_h = []

for i in range(n):
    m = int(input())

    if i%2==0:
        heapq.heappush(max_h, -m)
    else:
        heapq.heappush(min_h, m)
    
    if min_h:
        if -max_h[0] > min_h[0]:
            max_value = -heapq.heappop(max_h)
            min_value = heapq.heappop(min_h)

            heapq.heappush(min_h, max_value)
            heapq.heappush(max_h, -min_value)
            
    print(-max_h[0])