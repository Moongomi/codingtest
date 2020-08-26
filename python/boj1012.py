import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global A,m,n
    visit[x][y] = 1
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m and A[nx][ny] == 1 and visit[nx][ny] == 0:
                dfs(nx,ny)

T = int(input())
for q in range(T):
    cnt = 0
    m,n,k = map(int,input().split())
    A = [[0]*m for j in range(n)]
    visit = [[0]*m for j in range(n)]
    for z in range(k):
        i,j = map(int,input().split())
        A[j][i] = 1
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1 and visit[i][j] == 0:
                dfs(i,j)
                cnt+= 1
    print(cnt)
