# 1167번 트리의 지름 https://www.acmicpc.net/problem/1167
from collections import deque
v = int(input())
graph = [set() for _ in range(v + 1)]
for _ in range(v):
    info = list(map(int, input().split()))
    n1 = info[0]
    for i in range(1, len(info) - 1, 2):
        n2, cost = info[i], info[i + 1]
        graph[n1].add((n2, cost))
        graph[n2].add((n1, cost))
# 처음 한 노드에 대해 탐색해서 가장 먼 노드를 찾자
init_node = 1
for _ in range(2):
    max_node = init_node
    max_dist = 0
    visited = [False] * (v + 1)
    q = deque()
    q.append((max_node, 0))
    visited[max_node] = True
    while q:
        node, cost = q.popleft()
        for n_node, dist in graph[node]:
            if not visited[n_node]:
                visited[n_node] = True
                q.append((n_node, cost + dist))
                if cost + dist > max_dist:
                    max_node = n_node
                    max_dist = cost + dist
    init_node = max_node
print(max_dist)





# result = 0
# for leaf in leafs:
#     visited = [False] * (v + 1)
#     q = deque()
#     q.append((leaf, 0))
#     visited[leaf] = True
#     while q:
#         node, cost = q.popleft()
#         for n_node, dist in graph[node]:
#             if not visited[n_node]:
#                 visited[n_node] = True
#                 q.append((n_node, cost + dist))
#         result = max(result, cost)
# print(result)

