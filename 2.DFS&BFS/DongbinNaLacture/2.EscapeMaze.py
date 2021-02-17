from collections import deque

n, m = map(int, input().split())
graph = []
successes = []
for i in range(n):
    graph.append(list(map(bool, map(int, list(input())))))


def explore(x, y, move, cache):
    if x <= -1 or x >= n or y <= -1 or y >= m or (not graph[x][y]) or ("{0},{1}".format(x, y) in cache):
        return
    elif x == n - 1 and y == m - 1:
        successes.append(move)
    else:
        explore(x - 1, y, move + 1, cache + " {0},{1}".format(x, y))
        explore(x + 1, y, move + 1, cache + " {0},{1}".format(x, y))
        explore(x, y - 1, move + 1, cache + " {0},{1}".format(x, y))
        explore(x, y + 1, move + 1, cache + " {0},{1}".format(x, y))


explore(0, 0, 1, "")
print(min(successes))


# 예시 코드
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


