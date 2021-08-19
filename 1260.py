from sys import stdin

def dfs(v):
    dfs_visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if(dfs_visited[i] == 0 and matrix[v][i] == 1):
            dfs(i)
def bfs(v):
    que = [v]
    bfs_visited[v] = 1
    while que:
        v = que.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if(bfs_visited[i] == 0 and matrix[v][i] == 1):
                que.append(i)
                bfs_visited[i] = 1
                
n, m, v = map(int, stdin.readline().split())
matrix = [ [0] * (n+1) for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
    
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

dfs(v)
print()
bfs(v)

