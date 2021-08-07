from sys import stdin

n = int(stdin.readline().strip())

arr = list(map(int, stdin.readline().split()))

arr.sort(reverse = True)

total = 0
for i in arr:
    if arr[0] != i:
        total += i / 2
print(sum(arr) - total)
