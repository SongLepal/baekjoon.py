from sys import stdin
from math import factorial

t = int(stdin.readline().strip())

for _ in range(t):
    n, m = map(int, stdin.readline().split(' '))
    cnt = factorial(m) // (factorial(m-n) * factorial(n))
    print(cnt)
    
