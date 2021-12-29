import sys
import collections
input = sys.stdin.readline

def bfs():
    global arr
    q = collections.deque()
    q.append([0,0])
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if cheeze[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                elif cheeze[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = 1
                    cheeze[nx][ny] = 0
    arr.append(cnt)
    return cnt

n,m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
arr = []

while True:
    # 남아있는 치즈가 없으면 끝
    count = bfs()
    if count == 0:
        # while문 돌리면서 time 변수 +1로 계산 가능
        print(len(arr)-1)
        print(arr[-2])
        break
