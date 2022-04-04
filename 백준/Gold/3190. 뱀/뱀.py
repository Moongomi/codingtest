import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [[0]*(n+1) for _ in range(n+1)]
q = deque()

for _ in range(k):
    x,y = map(int,input().split())
    board[x][y] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    x = int(x)
    q.append([x,c])

cnt = 0
d = 0
mx = 1
my = 1

board[mx][my] = 2
t = q.popleft()
bam = [(mx,my)]
while True:
    nx = mx + dx[d]
    ny = my + dy[d]

    if 1<=nx<=n and 1 <=ny<=n and board[nx][ny] != 2:
        if board[nx][ny] == 0:
            tx,ty = bam.pop(0)
            board[tx][ty] = 0
        board[nx][ny] = 2
        bam.append((nx,ny))

    else:
        cnt+=1
        break

    mx, my = nx, ny
    cnt += 1

    if cnt in t:
        if t[1] == 'D':
            d += 1
        elif t[1] == 'L':
            d -=1
        d %= 4
        if q:
            t = q.popleft()

print(cnt)