# https://www.acmicpc.net/problem/10026
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(input()) for _ in range(n)]
# 정상인의 결과
result1 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            result1 += 1
            temp_color = graph[i][j]
            stack = [(i, j)]
            while stack:
                y, x = stack.pop()
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] == temp_color:
                        visited[ny][nx] = True
                        stack.append((ny, nx))
# 적록색약 결과
result2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            result2 += 1
            temp_colors = ['R', 'G'] if graph[i][j] in ['R', 'G'] else ['B']
            stack = [(i, j)]
            while stack:
                y, x = stack.pop()
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] in temp_colors:
                        visited[ny][nx] = True
                        stack.append((ny, nx))
print(result1, result2)



