from sys import stdin

n = int(stdin.readline().strip())

arr = list(map(int, stdin.readline().split()))

if n % 2:
    arr.append(0)
arr.sort()

m = 0
for i in range(len(arr)//2):
    m = max(m, arr[i] + arr[len(arr)-i-1])
print(m)
