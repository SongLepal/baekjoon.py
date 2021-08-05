from sys import stdin

n = int(stdin.readline().rstrip())
if n == 1 or n == 3:
    print(-1)
else:
    cnt = 0
    cnt += n // 5
    n %= 5
    if n == 0:
        print(cnt)
    elif n % 2 == 0:
        cnt += n // 2
        print(cnt)
    elif n % 2 != 0:
        n += 5
        cnt += n // 2 - 1
        print(cnt)

