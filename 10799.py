from sys import stdin

_input = stdin.readline().strip()

isOpen = 0
stack = []
cnt = 0

for i in range(len(_input)):
    if _input[i] == '(':
        isOpen = 1
        stack.append('(')
    else:
        stack.pop()
        if isOpen:
            cnt += len(stack)
        else:
            cnt += 1
        isOpen = 0
        
print(cnt)
