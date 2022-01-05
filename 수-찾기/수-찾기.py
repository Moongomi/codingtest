N = int(input())
A = set(map(int,input().split()))
M = int(input())
temp = list(map(int,input().split()))
for _ in temp:
    if _ in A:
        print(1)
    else:
        print(0)
