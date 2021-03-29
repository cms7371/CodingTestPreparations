# 16236번 아기 상어 https://www.acmicpc.net/problem/16236

from collections import deque
offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
size = 2
eaten_num = 0
time = 0
fishes = [0] * 7
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            start_position = (i, j)
        elif graph[i][j] != 0:
            fishes[graph[i][j]] += 1
while any([fishes[i] for i in range(min(size, 7))]):
    q = deque()
    q.append(start_position + tuple([0]))
    results = []
    visited = [[False] * n for _ in range(n)]
    visited[start_position[0]][start_position[1]] = True
    while q:
        x, y, t = q.popleft()
        for o in offsets:
            nx, ny, nt = x + o[0], y + o[1], t + 1
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if 0 < graph[nx][ny] < size:
                    results.append((nt, nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 0 or graph[nx][ny] == size:
                    q.append((nx, ny, nt))
                    visited[nx][ny] = True
    if not results:  # 물고기가 있지만 도달하지 못하는 경우를 없애줘야함
        break
    results.sort()
    nt, nx, ny = results[0]
    time += nt
    fishes[graph[nx][ny]] -= 1
    graph[nx][ny] = 0
    start_position = (nx, ny)
    eaten_num += 1
    if eaten_num == size:
        eaten_num = 0
        size += 1
print(time)
