# https://www.acmicpc.net/problem/11404
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(10e9)
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    s, e, c = map(int, input().split())
    s -= 1
    e -= 1
    graph[s][e] = min(graph[s][e], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif graph[i][j] >= INF:
            graph[i][j] = 0
for line in graph:
    print(*line)