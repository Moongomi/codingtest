from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])
    cnt = 0
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
                cnt+=1
    return cnt-1

graph = {}
com = int(input())
edge = int(input())
start = 1

for i in range(edge):
    n1,n2 = map(int,input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(BFS(graph, start))
