# 문제 : 1150번 백업 https://www.acmicpc.net/problem/1150
# 솔루션 https://latter2005.tistory.com/34
import heapq


n, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]

q = []
result = []
visited = [False] * n
for i in range(n-1):
    heapq.heappush(q, (tuple([graph[i + 1] - graph[i], i, i + 1])))
while len(result) != k:
    dis, a, b = heapq.heappop(q)
    escape = False
    if visited[a] or visited[b]:
        continue
    result.append((dis, a, b))
    visited[a], visited[b] = True, True
    if a != 0 and b != n - 1:
        heapq.heappush(q, (graph[a] - graph[a - 1] + graph[b + 1] - graph[b] - dis, a - 1, b + 1))
output = 0
for r in result:
    output += r[0]
print(output)
