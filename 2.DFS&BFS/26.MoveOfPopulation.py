# 16234번 인구 이동 https://www.acmicpc.net/problem/16234
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
while True:
    unified = [[False] * n for _ in range(n)]
    unions = []
    for i in range(n):
        for j in range(n):
            if not unified[i][j]:
                for o1 in offsets[:2]:
                    ni, nj = i + o1[0], j + o1[1]
                    if ni < n and nj < n and not unified[ni][nj] and l <= abs(graph[i][j] - graph[ni][nj]) <= r:
                        q = deque()
                        q.append((i, j))
                        unified[i][j] = True
                        unions.append([(i, j)])
                        while q:
                            x, y = q.popleft()
                            for o2 in offsets:
                                nx, ny = x + o2[0], y + o2[1]
                                if 0 <= nx < n and 0 <= ny < n and not unified[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                                    unified[nx][ny] = True
                                    unions[-1].append((nx, ny))
                                    q.append((nx, ny))
    if not unions:
        break
    result += 1
    for union in unions:
        local_sum = sum([graph[i[0]][i[1]] for i in union]) // len(union)
        for c in union:
            graph[c[0]][c[1]] = local_sum
print(result)
print("\n".join(map(str, graph)))




