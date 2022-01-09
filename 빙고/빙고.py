import sys
input = sys.stdin.readline

pan = {}
visited = [[0]*5 for _ in range(5)]
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        pan[arr[j]] = (i, j)

cnt = 0
flag = False
for _ in range(5):
    arr = list(map(int, input().split()))
    for i in range(5):
        cnt +=1
        if arr[i] in pan:
            visited[pan[arr[i]][0]][pan[arr[i]][1]] = 1
            answer = 0
            for j in range(5):
                if sum(visited[j]) == 5:
                    answer += 1

                if sum([temp[j] for temp in visited]) == 5:
                    answer += 1

            if visited[0][4]+visited[1][3]+visited[2][2]+visited[3][1]+visited[4][0] == 5:
                answer += 1
            if visited[0][0]+visited[1][1]+visited[2][2]+visited[3][3]+visited[4][4] == 5:
                answer += 1

            if answer >=3:
                print(cnt)
                flag = True
                break
    if flag:
        break


