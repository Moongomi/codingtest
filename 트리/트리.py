import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = int(input())
tree = {}
leaf = 0

for i in range(n):
    # 지워지게 될 노드는 트리에 추가하지 않는다.
    if arr[i] == -1:
        root = i
    if i == d or arr[i] == d:
        continue
    # tree 만드는 부분
    if arr[i] not in tree:
        tree[arr[i]] = [i]
    else:
        tree[arr[i]].append(i)
# 지우는 노드가 루트 노드면 리프 노드는 당연히 0이므로 아닌 경우에만 계산
if d != root:
    queue = [-1]
    while queue:
        y = queue.pop()
        if y in tree:
            queue += tree[y]
        else:
            leaf += 1
print(leaf)
