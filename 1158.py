from sys import stdin

n, k = stdin.readline().split()
n = int(n); k = int(k);


num = 0
result = []
arr = [i for i in range(1, n+1)]

for i in range(n):
    num += k - 1
    if num >= len(arr):
        num %= len(arr)
    result.append(str(arr.pop(num)))
print("<",", ".join(result), ">", sep = '')
