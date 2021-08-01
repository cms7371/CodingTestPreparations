# 11559번 뿌요뿌요 https://www.acmicpc.net/problem/11559
from collections import deque
def pop():
    is_popped = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and not visited[i][j]:
                c = graph[i][j]
                visited[i][j] = True
                pop_list = [(i, j)]
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in offsets:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == c:
                            visited[nx][ny] = True
                            pop_list.append((nx, ny))
                            q.append((nx, ny))
                if len(pop_list) >= 4:
                    is_popped = True
                    for x, y in pop_list:
                        graph[x][y] = '.'

    return is_popped
def fall():
    for i in range(11, -1, -1):
        for j in range(6):
            if graph[i][j] == '.':
                di = 1
                while i - di >= 0:
                    if graph[i - di][j] != '.':
                        break
                    di += 1
                if i - di >= 0:
                    for l in range(i, di - 1, -1):
                        graph[l][j] = graph[l - di][j]
                    for l in range(di - 1, -1, -1):
                        graph[l][j] = '.'

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
graph = [list(input()) for _ in range(12)]
result = 0
while pop():
    result += 1
    fall()
print(result)