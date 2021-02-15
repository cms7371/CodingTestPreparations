import heapq

INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
queue = []
distances = [INF] * (n + 1)
heapq.heappush(queue, (0, c))
while queue:
    dis, node = heapq.heappop(queue)
    if distances[node] < dis:
        continue
    for i in graph[node]:
        new_dis = i[1] + dis
        if new_dis < distances[i[0]]:
            distances[i[0]] = new_dis
            heapq.heappush(queue, (new_dis, i[0]))
count = 0
max_dis = 0
for d in distances:
    if d != INF:
        count += 1
        if max_dis < d:
            max_dis = d
print(count, max_dis)


