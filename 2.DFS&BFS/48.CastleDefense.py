# 17135번 캐슬 디펜스 https://www.acmicpc.net/problem/17135
from itertools import combinations
from collections import deque
offsets = [(0, -1), (-1, 0), (0, 1)]
n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
archer_combination = combinations(range(m), 3)
output = 0
for archer_positions in archer_combination:
    result = 0
    now_graph = [graph[i][:] for i in range(n)]
    for i in range(n - 1, -1, -1):
        victims = []
        for j in archer_positions:
            q = deque()
            q.append((i, j, 1))
            while q:
                x, y, dist = q.popleft()
                if now_graph[x][y] == 1:
                    victims.append((x, y))
                    break
                for dx, dy in offsets:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and dist < d:
                        q.append((nx, ny, dist + 1))
        for x, y in victims:
            if now_graph[x][y] == 1:
                now_graph[x][y] = 0
                result += 1
    output = max(output, result)
print(output)
