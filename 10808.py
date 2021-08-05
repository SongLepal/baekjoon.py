from sys import stdin

_input = stdin.readline().strip()
alpha = [ 0 for _ in range(26) ]

for i in _input:
    alpha[ord(i)-ord('a')] += 1

for i in range(26):
    print(alpha[i], end =' ')
