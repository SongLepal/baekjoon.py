from sys import stdin
from collections import deque

test = int(stdin.readline().strip())

que = deque()
for _ in range(test):
    while que:
        que.pop()
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    for i in arr:
        que.append(i)
    arr = [0 for _ in range(n)]
    arr[k] = 1
    cnt = 0
    while que:
        if que[0] == max(que):
            cnt += 1
            if arr[0] == 1:
                print(cnt)
                break
            else:
                que.popleft()
                del arr[0]
        else:
            que.append(que.popleft())
            arr.append(arr[0])
            del arr[0]
