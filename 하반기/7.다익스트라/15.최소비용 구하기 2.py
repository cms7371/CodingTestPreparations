# https://www.acmicpc.net/problem/11779
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
start, end = map(int, input().split())
dist = [INF] * (N + 1)
prev_node = [-1] * (N + 1)
dist[start] = 0
prev_node[start] = start
pq = [(0, start)]
while pq:
    d, cur = heappop(pq)
    if d <= dist[cur]:
        for _next, dd in graph[cur]:
            if d + dd < dist[_next]:
                dist[_next] = d + dd
                prev_node[_next] = cur
                heappush(pq, (d + dd, _next))
stack = [end]
while True:
    if prev_node[stack[-1]] != stack[-1]:
        stack.append(prev_node[stack[-1]])
    else:
        break
print(dist[end])
print(len(stack))
print(*stack[::-1])

