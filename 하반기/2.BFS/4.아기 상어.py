# https://www.acmicpc.net/problem/16236
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 아기 상어 시작 위치 잧음
cnt_y, cnt_x = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            cnt_y, cnt_x = i, j
            graph[i][j] = 0
result = 0
cnt_size = 2
cnt_eaten = 0
while True:
    # 가까운 먹을 수 있는 물고기들을 탐색함
    min_dist = 10e9  # 최대한 가까운 물고기의 거리
    fishes = []  # 가까운 물고기들의 수
    visited = [[False] * n for _ in range(n)]  # 방문 체크
    visited[cnt_y][cnt_x] = True
    q = deque()
    q.append((cnt_y, cnt_x, 0))
    while q:
        y, x, dist = q.popleft()
        if dist >= min_dist:
            continue
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == 0 or graph[ny][nx] == cnt_size:
                    q.append((ny, nx, dist + 1))
                elif graph[ny][nx] < cnt_size:
                    fishes.append((ny, nx))
                    min_dist = dist + 1
    if fishes:
        fishes.sort()
        cnt_y, cnt_x = fishes[0]
        graph[cnt_y][cnt_x] = 0
        result += min_dist
        cnt_eaten += 1
        if cnt_eaten >= cnt_size:
            cnt_eaten = 0
            cnt_size += 1
    else:
        break
print(result)

