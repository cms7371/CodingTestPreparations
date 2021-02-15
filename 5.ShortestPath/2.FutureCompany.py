# 내 코드 dijkstra 2번 이용
def dijkstra(s):
    q = []
    visited = [False] * (n + 1)
    visited[s] = True
    distances = [INF] * (n + 1)
    distances[s] = 0
    q.append(s)
    while q:
        now = q.pop(0)
        dis = distances[now]
        for i in graph[now]:
            if visited[i]:
                continue
            else:
                visited[i] = True
                distances[i] = dis + 1
                q.append(i)
    return distances


INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
x, k = map(int, input().split())

origin_distances = dijkstra(1)
print(origin_distances)
via_distances = dijkstra(k)
print(via_distances)
result = origin_distances[k] + via_distances[x]
if result >= INF:
    print(-1)
else:
    print(result)

# 예시 코드
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n+1):
    graph[a][a] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)

