from sys import stdin

n = int(stdin.readline().rstrip())

dist = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))

total = 0
oil = cost[0]
for i in range(n-1):
    oil = min(oil, cost[i])
    total += oil * dist[i]
print(total)
