# 11725번 부모 노드 찾기
from collections import deque
n = int(input())
graph = dict()
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = {b}
    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = {a}
q = deque([1])
visited[1] = 1
while q:
    current_node = q.popleft()
    for next_node in graph[current_node]:
        if visited[next_node] == 0:
            visited[next_node] = current_node
            q.append(next_node)
print("\n".join(map(str, visited[2:])))




