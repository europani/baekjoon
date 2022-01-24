data = input()
stack = []

for x in data:
    if x in ('+', '-'):
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(x)
    elif x in ('*', '/'):
        while stack and stack[-1] in ('*', '/'):
            print(stack.pop(), end='')
        stack.append(x)
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    else:
        print(x, end='')

while stack:
    print(stack.pop(), end='')