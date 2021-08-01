# 3190번 뱀 https://www.acmicpc.net/problem/3190
from collections import deque
import sys
input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오, 아래, 왼, 위 순서
n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2
control = []
k = int(input())
for _ in range(k):
    t, d = input().split()
    t = int(t)
    control.append((t, d))
body = deque()
body.append((0, 0))
d = 0
time = 0
graph[0][0] = 1
idx = 0
while True:
    time += 1
    x, y = body[-1]
    nx, ny = x + directions[d][0], y + directions[d][1]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1:
        body.append((nx, ny))
        if graph[nx][ny] == 0:
            rx, ry = body.popleft()
            graph[rx][ry] = 0
        graph[nx][ny] = 1
    else:
        break
    if idx < len(control) and control[idx][0] == time:
        if control[idx][1] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        idx += 1
print(time)
