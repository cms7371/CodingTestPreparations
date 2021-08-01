# 1389번 케빈 베이컨의 6단계 법칙 https://www.acmicpc.net/problem/1389
# 두번째 : 플로이드 워셜 알고리즘 이용
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != 0:
            for k in range(n + 1):
                if graph[j][k] != 0:
                    if graph[i][k] == 0:
                        graph[i][k] = graph[i][j] + graph[j][k]
                    else:
                        graph[i][k] = min(graph[i][k], graph[i][j] + graph[j][k])
                    graph[k][i] = graph[i][k]
result = 0
val = 10e9
for i in range(1, n + 1):
    graph[i][i] = 0
    local_val = sum(graph[i])
    if local_val < val:
        val = local_val
        result = i
print(result)

# 첫번째 : 다익스트라 모든 노드에 대해 돌려보기
from heapq import heappop, heappush
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
kevin_val = 10e9
output = 0
for i in range(1, n + 1):
    q = []
    visited = [0] * (n + 1)
    visited[0], visited[i] = -1, -1
    for j in graph[i]:
        heappush(q, (1, j))
    while not all(visited):
        dist, current_node = heappop(q)
        if not visited[current_node]:
            visited[current_node] = dist
            for next_node in graph[current_node]:
                if not visited[next_node]:
                    heappush(q, (dist + 1, next_node))
    result = sum(visited) + 2
    if result < kevin_val:
        kevin_val = result
        output = i
print(output)

