# 1260번 DFS와 BFS
from collections import deque
n, m, v = map(int, input().split())
graph = dict()
for _ in range(m):
    s, e = map(int, input().split())
    if s not in graph:
        graph[s] = set()
    if e not in graph:
        graph[e] = set()
    graph[s].add(e)
    graph[e].add(s)
if v not in graph:
    print(v)
    print(v)
else:
    stack = deque()
    visited = dict()
    for n in graph:
        visited[n] = False
    stack.append(v)
    DFS = []
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        DFS.append(str(node))
        next_nodes = list(graph[node])
        next_nodes.sort(reverse=True)
        for n in next_nodes:
            if not visited[n]:
                stack.append(n)
    print(" ".join(DFS))

    q = deque()
    visited = dict()
    for n in graph:
        visited[n] = False
    q.append(v)
    BFS = []
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        BFS.append(str(node))
        next_nodes = list(graph[node])
        next_nodes.sort()
        for n in next_nodes:
            if not visited[n]:
                q.append(n)
    print(" ".join(BFS))

