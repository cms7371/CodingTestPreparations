# 2644번 촌수 계산 https://www.acmicpc.net/problem/2644

from collections import deque
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
q = deque()
q.append((start, 0))
visited[start] = True
result = -1
while q:
    current_node, distance = q.popleft()
    if current_node == end:
        result = distance
        break
    for next_node in range(n + 1):
        if graph[current_node][next_node] and not visited[next_node]:
            q.append((next_node, distance + 1))
            visited[next_node] = True
print(result)
