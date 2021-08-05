from sys import stdin

_input = stdin.readline().strip()

stack = []
cnt = 0
result = []

for i in _input:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '/' or stack[-1] == '*'):
            result.append(stack.pop())
        stack.append(i)
    else:
        result.append(i)
while stack:
    result.append(stack.pop())

for i in result:
    print(i, end = '')
