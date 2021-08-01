# https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus_p, empty_p = [], []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_p.append((i, j))
        elif graph[i][j] == 2:
            virus_p.append((i, j))
cases = combinations(empty_p, 3)
result = 0
for wall_p in cases:
    cnt_graph = [line[:] for line in graph]
    for y, x in wall_p:
        cnt_graph[y][x] = 1
    # 바이러스를 퍼뜨리고
    q = deque(virus_p)
    while q:
        y, x = q.popleft()
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and cnt_graph[ny][nx] == 0:
                cnt_graph[ny][nx] = 2
                q.append((ny, nx))
    # 안전 공간을 카운트
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if cnt_graph[i][j] == 0:
                safe_area += 1
    # 그리고 결과에 업데이트
    result = max(result, safe_area)
print(result)

