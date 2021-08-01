# 1987번 알파벳 https://www.acmicpc.net/problem/1987

# BFS -> 시간 초과...
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
# Stack이 아닌 테이블을 이용하는 것으로 비교 횟수를 줄임 그지같네 진짜
alpha = [False] * 28
cnt = 0
result = 0
def dfs(x, y):
    alpha[ord(graph[x][y]) - 65] = True
    global result, cnt
    cnt += 1
    result = max(result, cnt)
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] and not alpha[ord(graph[nx][ny]) - 65]:
            dfs(nx, ny)
    alpha[ord(graph[x][y]) - 65] = False
    cnt -= 1
dfs(0, 0)
print(result)

# BFS
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
q = deque()
q.append((0, 0, tuple(graph[0][0])))
result = 1
while q:
    x, y, path = q.popleft()
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] not in path:
            result = max(result, len(path) + 1)
            q.append((nx, ny, (*path, graph[nx][ny])))
print(result)



