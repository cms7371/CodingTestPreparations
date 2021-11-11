# https://www.acmicpc.net/problem/1197
import sys
input = sys.stdin.readline


# 크루스칼 풀이
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    if find(a) < find(b):
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b)



V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((w, s, e))
edges.sort()
parent = [i for i in range(V + 1)]
result = 0
for w, s, e in edges:
    if find(s) != find(e):
        result += w
        union(s, e)
print(result)

# 프림 알고리즘
from heapq import *
import sys
input = sys.stdin.readline



V, E = map(int, input().split())
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    edges[s].append((w, s, e))
    edges[e].append((w, s, e))
visited = [False] * (V + 1)
visited[1] = True
result = 0
q = []
for path in edges[1]:
    heappush(q, path)
while q:
    w, s, e = heappop(q)
    for node in (s, e):
        if not visited[node]:
            visited[node] = True
            result += w
            for path in edges[node]:
                heappush(q, path)
print(result)





