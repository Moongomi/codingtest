import sys
input = sys.stdin.readline

n = int(input())
arr = []
win = []
for i in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
    win.append([i+1,0])

for i in range(n-1):
    for j in range(i,n):

        p1 = arr[i][0] + arr[j][0] * arr[i][1]
        p2 = arr[j][0] + arr[i][0] * arr[j][1]

        if p1 > p2:
            win[i][1] += 1
        elif p1 < p2:
            win[j][1] += 1

win = sorted(win, key=lambda x:x[1], reverse=True)
for i in range(n):
    print(win[i][0])

