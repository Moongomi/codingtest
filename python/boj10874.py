import sys
inputLine = sys.stdin.readline

N = int(input())
answer = [0]*10
for j in range(0,10):
    answer[j] = (j% 5)+1

solve = [list(map(int, input().split())) for _ in range(N)]

for i in range(0,N):
    if answer == solve[i]:
        print(i+1)
