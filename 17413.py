from sys import stdin

intag = 0
stack = []
_str = stdin.readline().strip()

for i in range(len(_str)):
    if _str[i] == '<':
        intag = 1
        while stack:
            print(stack.pop(), end = '')
        print('<', end = '')
    elif _str[i] == '>':
        intag = 0
        print('>', end = '')
    elif intag:
        print(_str[i], end ='')
    elif not intag:
        if _str[i] == ' ':
            while stack:
                print(stack.pop(), end = '')
            print(' ', end ='')
        else:
            stack.append(_str[i])
while stack:
    print(stack.pop(), end ='')

