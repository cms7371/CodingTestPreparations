# 1937번 욕심쟁이 판다 https://www.acmicpc.net/problem/1937
# 다른 방법 -> 가장 높은 자리부터 탐색함. 주변에 자신보다 큰 숫자가 있으면 그 숫자 + 1
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
search_order = []
for i in range(n):
    for j in range(n):
        search_order.append((graph[i][j], i, j))
search_order.sort(reverse=True)
for _, x, y in search_order:
    local_max = 0
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            local_max = max(dp[nx][ny], local_max)
    dp[x][y] = local_max + 1
print(max([max(i) for i in dp]))


# 탐색 개같은거 시간 초과 오질라게 남
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = 0
search_order = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            q = deque()
            q.append((i, j, 1))
            visited[i][j] = 1
            while q:
                x, y, day = q.popleft()
                for o in offsets:
                    nx, ny = x + o[0], y + o[1]
                    if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny] and visited[nx][ny] < day + 1:
                        if not visited[nx][ny]:
                            q.append((nx, ny, day + 1))
                            visited[nx][ny] = day + 1
print(max([max(i) for i in visited]))
