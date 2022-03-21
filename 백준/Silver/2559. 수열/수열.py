n, size = map(int, input().split())
degrees = list(map(int, input().split()))

left = 0
right = left+size

sub_sum = sum(degrees[left:right])
answer = sub_sum

while right < n:
    sub_sum+=degrees[right]-degrees[left]
    answer = max(sub_sum, answer)

    left+=1
    right+=1
print(answer)