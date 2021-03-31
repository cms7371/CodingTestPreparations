# 1967번 트리의 지름 https://www.acmicpc.net/problem/1967
from collections import deque
n = int(input())
node_weight = [0] * (n + 1)
edge = [[] for _ in range(n + 1)]
result = 0
parents = [i for i in range(n + 1)]
queued = [False] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    edge[p].append((c, w))
    parents[c] = p
q = deque()
for i in range(1, n + 1):
    if len(edge[i]) == 0:
        visited[i] = True
        if not queued[parents[i]]:
            queued[parents[i]] = True
            q.append(parents[i])
result = 0
while q:
    node = q.popleft()
    skip = False
    weights = []
    for c, w in edge[node]:
        if not visited[c]:
            skip = True
            break
        weights.append(node_weight[c] + w)
    if skip:
        q.append(node)
        continue
    visited[node] = True
    weights.sort()
    if not weights:
        continue
    node_weight[node] = weights[-1]
    if len(weights) >= 2:
        result = max(result, weights[-1] + weights[-2])
    elif len(weights) == 1:
        result = max(result, weights[-1])
    if not queued[parents[node]] and parents[node] != node:
        queued[parents[node]] = True
        q.append(parents[node])
print(result)





