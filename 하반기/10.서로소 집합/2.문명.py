# https://www.acmicpc.net/problem/14868
import sys
input = sys.stdin.readline


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    if find(a) > find(b):
        cul.remove(find(a))
        p[find(a)] = find(b)
    elif find(a) < find(b):
        cul.remove(find(b))
        p[find(b)] = find(a)


offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, K = map(int, input().split())
graph = [[0] * N for _ in range(N)]
p = [i for i in range(K + 1)]
cul = set()
bound = []
for i in range(1, K + 1):
    y, x = map(lambda s: int(s) - 1, input().split())
    graph[y][x] = i
    cul.add(i)
    bound.append((y, x, i))
t = 0
while True:
    n_bound = []
    for y, x, i in bound:
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] != 0 and find(graph[ny][nx]) != find(i):
                union(graph[ny][nx], i)
    if len(cul) == 1:
        break
    t += 1
    for y, x, i in bound:
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = find(i)
                    n_bound.append((ny, nx, find(i)))
                elif find(graph[ny][nx]) != find(i):
                    union(graph[ny][nx], i)
    bound = n_bound
print(t)