# 14502번 연구소 https://www.acmicpc.net/problem/14502
# 입력이 8 * 8 이내로 브루트포스를 이용할 수 있는
from itertools import combinations
from collections import deque

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(n)]
empty = []
virus = []
result = 0
for i in range(n):
    for j in range(m):
        if original[i][j] == 0:
            empty.append((i, j))
        elif original[i][j] == 2:
            virus.append((i, j))
for case in combinations(empty, 3):
    graph = []
    for line in original:
        graph.append([i for i in line])
    for wall in case:
        graph[wall[0]][wall[1]] = 1
    q = deque()
    for v in virus:
        q.append(v)
    while q:
        x, y = q.popleft()
        for o in offsets:
            nx, ny = x + o[0], y + o[1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
    result = max(result, sum([i.count(0) for i in graph]))
print(result)
