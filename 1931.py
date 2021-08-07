from sys import stdin

n = int(stdin.readline().strip())

arr = []
cnt = 1
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    arr.append((a, b))

arr.sort(key = lambda x: (x[1], x[0]))
end = arr[0][1]

for i in range(1, n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]
print(cnt)
    

        
