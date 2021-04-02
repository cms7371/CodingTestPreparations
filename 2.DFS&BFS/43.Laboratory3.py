# 17142번 연구소 3 https://www.acmicpc.net/problem/17142
from itertools import combinations
offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus_p = []
empty_c = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            empty_c += 1
        elif graph[i][j] == 2:
            virus_p.append((i, j))
virus_case = combinations(virus_p, m)
result = 10e9 if empty_c != 0 else 0
for current_virus in virus_case:
    virus_num = 0
    now_graph = [graph[i][:] for i in range(n)]
    inactive_virus = [v for v in virus_p if v not in current_virus]
    for i, j in inactive_virus:
        now_graph[i][j] = 3
    time = 0
    while True:
        next_virus = []
        for x, y in current_virus:
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if now_graph[nx][ny] == 0:
                        now_graph[nx][ny] = 2
                        virus_num += 1
                        next_virus.append((nx, ny))
                    elif now_graph[nx][ny] == 3:
                        now_graph[nx][ny] = 2
                        next_virus.append((nx, ny))
        if not next_virus:
            break
        time += 1
        if virus_num == empty_c:
            break
        current_virus = next_virus
    if virus_num == empty_c:
        result = min(result, time)
print(-1 if result == 10e9 else result)
