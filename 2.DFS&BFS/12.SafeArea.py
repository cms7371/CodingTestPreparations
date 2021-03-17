# 2468번 안전 영역 https://www.acmicpc.net/problem/2468
from collections import deque
offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
n = int(input())
original = []
case = set()
for _ in range(n):
    line = list(map(int, input().split()))
    original.append(line)
    case = case.union(set(line))
output = 1
for rain in case:
    graph = []
    for line in original:
        graph.append([i for i in line])
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain:
                result += 1
                q = deque()
                q.append((i, j))
                graph[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for o in offsets:
                        nx, ny = x + o[0], y + o[1]
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > rain:
                            graph[nx][ny] = 0
                            q.append((nx, ny))
    output = max(output, result)
print(output)



