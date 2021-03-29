# 3055번 탈출 https://www.acmicpc.net/problem/3055

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
flood_area = []
current_position = []
visited = [[False] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'D':
            destination = (i, j)
        elif graph[i][j] == '*':
            flood_area.append((i, j))
        elif graph[i][j] == "S":
            current_position.append((i, j))
            visited[i][j] = True
result = -1
time = 0
stop = False
while current_position and not stop:
    time += 1
    next_flood_area = []
    for f in flood_area:
        for o in offsets:
            nx, ny = f[0] + o[0], f[1] + o[1]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == ".":
                next_flood_area.append((nx, ny))
                graph[nx][ny] = "*"
    flood_area = next_flood_area
    next_position = []
    for p in current_position:
        for o in offsets:
            nx, ny = p[0] + o[0], p[1] + o[1]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if (nx, ny) == destination:
                    result = time
                    stop = True
                    break
                elif graph[nx][ny] == ".":
                    next_position.append((nx, ny))
                    visited[nx][ny] = True
    current_position = next_position
print("KAKTUS" if result == -1 else result)

