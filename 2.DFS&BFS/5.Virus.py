# 2606번 바이러스 https://www.acmicpc.net/problem/2606
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
stack = [1]
count = 0
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        count += 1
        for i in graph[node]:
            stack.append(i)
print(count - 1)


