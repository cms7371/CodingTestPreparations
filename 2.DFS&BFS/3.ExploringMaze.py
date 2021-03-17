# 2178번 미로 탐색 https://www.acmicpc.net/problem/2178
# BFS를 이용하여 최단 횟수를 찾아내는 풀이
from collections import deque
offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
print(graph[-1][-1])








