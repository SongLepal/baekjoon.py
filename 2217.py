from sys import stdin

n = int(stdin.readline().rstrip())

rope = []

for _ in range(n):
    rope.append(int(stdin.readline().rstrip()))
rope.sort(reverse = True)

power = 0
for i in range(n):
    power = max(power, rope[i] * (i + 1))
print(power)
