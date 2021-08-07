from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))
arr.sort()

total = 0
for i in range(n):
    total += arr[i] * (n-i)
    
print(total)
