from sys import stdin

n = int(stdin.readline().strip())

arr = []

for _ in range(n):
    arr.append(int(stdin.readline().strip()))
arr.sort(reverse = True)

_sum = 0
for i in range(1, n+1):
    if arr[i - 1] - (i - 1) > 0:
        _sum += arr[i - 1] - (i - 1)
    else:
        break
print(_sum)

