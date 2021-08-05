from sys import stdin

n = int(stdin.readline().strip())

que = []

for i in range(n):
    _input = stdin.readline().split()

    if _input[0] == 'push':
        que.insert(0, _input[1])
    elif _input[0] == 'pop':
        if len(que) != 0:
            print(que.pop())
        else:   print(-1)
    elif _input[0] == 'size':
        print(len(que))
    elif _input[0] == 'empty':
        if len(que) == 0:    print(1)
        else:   print(0)
    elif _input[0] == 'back':
        if len(que) == 0:   print(-1)
        else:   print(que[0])
    elif _input[0] == 'front':
        if len(que) == 0:   print(-1)
        else:   print(que[len(que)-1])
