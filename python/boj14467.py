import sys
input = sys.stdin.readline
N = int(input())
A = [2]*10
cnt = 0

for _ in range(N):
    num,dir = map(int,input().split())
    if A[num-1] != 2 and A[num-1] != dir:
        cnt+=1

    A[num-1] = dir

print(cnt)


