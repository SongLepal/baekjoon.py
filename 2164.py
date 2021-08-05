from sys import stdin
from collections import deque
n = int(stdin.readline().strip())

que = deque()
for i in range(n):
    que.append(i+1)

while True:
    if len(que) == 1:
        break
    que.popleft()
    que.append(que.popleft())
print(que.pop())
