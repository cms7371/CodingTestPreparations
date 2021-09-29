# https://www.acmicpc.net/problem/1956
import sys
input = sys.stdin.readline
INF = 10 ** 9


V, E = map(int, input().split())
graph = [[INF] * V for _ in range(V)]
for _ in range(E):
    s, e, d = map(int, input().split())
    s, e = s - 1, e - 1
    graph[s][e] = d
for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
answer = min(graph[i][i] for i in range(V))
print(-1 if answer == INF else answer)