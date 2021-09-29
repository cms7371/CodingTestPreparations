# https://www.acmicpc.net/problem/3197
from collections import deque


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    if find(a) > find(b):
        p[find(a)] = find(b)
    elif find(a) < find(b):
        p[find(b)] = find(a)


R, C = map(int, input().split())
graph = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
L_idx = []
count = 0
bound = []
for i in range(R):
    for j in range(C):
        if graph[i][j] != 'X' and not visited[i][j]:
            count += 1
            visited[i][j] = count
            q = deque()
            q.append((i, j))
            while q:
                y, x = q.popleft()
                if graph[y][x] == "L":
                    L_idx.append(count)
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C:
                        if graph[ny][nx] != 'X' and not visited[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = count
                        elif graph[ny][nx] == 'X':
                            bound.append((ny, nx, count))
p = [i for i in range(count + 1)]
t = 0
while True:
    if find(L_idx[0]) == find(L_idx[1]):
        break
    t += 1
    n_bound = []
    for y, x, idx in bound:
        if visited[y][x] != 0:
            union(visited[y][x], idx)
        else:
            visited[y][x] = find(idx)
            for dy, dx in offsets:
                ny, nx = y + dy, x + dx
                if 0 <= ny < R and 0 <= nx < C:
                    if visited[ny][nx] not in (0, idx):
                        union(visited[ny][nx], idx)
                    elif visited[ny][nx] == 0:
                        n_bound.append((ny, nx, find(idx)))

    bound = n_bound
print(t)