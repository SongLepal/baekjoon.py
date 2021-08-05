from sys import stdin
from collections import deque

n = int(stdin.readline().strip())

d = deque()

for i in range(n):
    _input = stdin.readline().split()

    if _input[0] == 'push_front':
        d.append(_input[1])
    elif _input[0] == 'push_back':
        d.appendleft(_input[1])
    elif _input[0] == 'pop_front':
        if not len(d) == 0: print(d.pop())
        else:   print(-1)
    elif _input[0] == 'pop_back':
        if not len(d) == 0: print(d.popleft())
        else:   print(-1)
    elif _input[0] == 'size':
        print(len(d))
    elif _input[0] == 'empty':
        if len(d) == 0:    print(1)
        else:   print(0)
    elif _input[0] == 'front':
        if not len(d) == 0: print(d[len(d)-1])
        else:   print(-1)
    elif _input[0] == 'back':
        if not len(d) == 0: print(d[0])
        else:   print(-1)
