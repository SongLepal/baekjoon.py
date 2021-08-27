from sys import stdin

read = stdin.readline

t = int(read().strip())

d = [0, 1, 2, 4]
nums = []

for _ in range(t):
    nums.append(int(read().strip()))

for i in range(4, max(nums)+1):
    d.append(d[i-1] + d[i-2] + d[i-3])
    
for i in range(t):
    print(d[nums[i]])
        
