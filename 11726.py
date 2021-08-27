from sys import stdin

read = stdin.readline

d = [0, 1, 2] # 3, 5
n = int(read().strip())

for i in range(3, n+1):
    d.append(d[i-1] + d[i-2])
print(d[n] % 10007)
