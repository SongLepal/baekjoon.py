from sys import stdin

read = stdin.readline

n = int(read().strip())
if n % 2 == 0:
    print('CY')
else:
    print('SK')
