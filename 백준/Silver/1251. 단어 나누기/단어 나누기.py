word = input()
result=[]

for i in range(1, len(word)-1):
    for j in range(1, len(word)-i):
        strs = [word[0:i], word[i:i+j], word[i+j:]]
        result.append(''.join(str[::-1] for str in strs))

print(sorted(result)[0])