import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])

mind = sys.maxsize
pick = list(combinations(chicken, m))
for i in range(len(pick)):
    dist = 0
    for h in home:
        dist += min([abs(h[0]-pick[i][j][0])+abs(h[1]-pick[i][j][1]) for j in range(m)])
    mind = min(mind, dist)
print(mind)