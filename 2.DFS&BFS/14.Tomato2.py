# 7569번 토마토 https://www.acmicpc.net/problem/7569
offsets = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append([list(map(int, input().split())) for _ in range(n)])
def ripen(a, b, c):
    for o in offsets:
        na, nb, nc = a + o[0], b + o[1], c + o[2]
        if 0 <= na < h and 0 <= nb < n and 0 <= nc < m and graph[na][nb][nc] == 0:
            next_tomato.add((na, nb, nc))
next_tomato = set()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                ripen(i, j, k)
day = 0
while next_tomato:
    day += 1
    current = next_tomato
    next_tomato = set()
    for c in current:
        graph[c[0]][c[1]][c[2]] = 1
    while current:
        ripen(*current.pop())
if all([all([all(j) for j in i]) for i in graph]):
    print(day)
else:
    print(-1)

