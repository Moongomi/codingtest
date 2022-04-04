import sys
input = sys.stdin.readline

n,k = map(int,input().split())
number = list(input().rstrip())
cnt = k
answer = []

for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        answer.pop()
        cnt-=1
    answer.append(num)
print(''.join(answer[:n-k]))