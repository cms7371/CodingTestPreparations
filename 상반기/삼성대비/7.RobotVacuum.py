# 14503번 로봇청소기 https://www.acmicpc.net/problem/14503
offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph[x][y] = -1
result = 1
while True:
    moved = False
    for nd in [(d - i) % 4 for i in range(1, 5)]:
        o = offsets[nd]
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            moved = True
            graph[nx][ny] = -1
            x, y = nx, ny
            result += 1
            d = nd
            break
    if moved:
        continue
    else:
        o = offsets[d]
        nx, ny = x - o[0], y - o[1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
            x, y = nx, ny
            continue
        else:
            break
print(result)




