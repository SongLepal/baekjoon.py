from sys import stdin

n = int(stdin.readline().strip())

arr = []

for _ in range(n):
    arr.append(int(stdin.readline().strip()))
arr.sort(reverse = True)

total = 0
for i in range(n):
    if i % 3 != 2:
        total += arr[i]
print(total)
