# https://www.acmicpc.net/problem/2458
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = True
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True
result = 0
for i in range(n):
    graph[i][i] = True
    is_ok = True
    for j in range(n):
        if not graph[i][j] and not graph[j][i]:
            is_ok = False
            break
    if is_ok: result += 1
print(result)
