# https://www.acmicpc.net/problem/2933
from collections import deque


def get_break_pos(height, fromLeft, graph):
    global C
    if fromLeft:
        i = 0
        while i < C and graph[height][i] != "x":
            i += 1
    else:
        i = C - 1
        while i >= 0 and graph[height][i] != "x":
            i -= 1
    if i == -1 or i == C:
        return None
    else:
        return height, i


offsets = [(0, 1), (-1, 0), (0, -1), (1, 0)]
R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]
N = int(input())
sticks = list(map(int, input().split()))
isLeft = True
for cur in sticks:
    stick_height = R - cur
    break_pos = get_break_pos(stick_height, isLeft, table)
    isLeft = not isLeft
    if not break_pos:
        continue
    table[break_pos[0]][break_pos[1]] = '.'
    for offset in offsets:
        iy, ix = break_pos[0] + offset[0], break_pos[1] + offset[1]
        if 0 <= iy < R and 0 <= ix < C and table[iy][ix] == 'x':
            cluster = [(iy, ix)]
            max_y = iy
            q = deque()
            q.append((iy, ix))
            visited = [[False] * C for _ in range(R)]
            visited[iy][ix] = True
            while q:
                y, x = q.popleft()
                for dy, dx in offsets:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C and table[ny][nx] == 'x' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        max_y = max(max_y, ny)
                        cluster.append((ny, nx))
                        q.append((ny, nx))
            if max_y == R - 1:
                continue
            down_h = 101
            for y, x in cluster:
                table[y][x] = '.'
                cur_drop = 0
                while y + cur_drop + 1 < R:
                    if visited[y + cur_drop + 1][x]:
                        cur_drop = 101
                        break
                    elif table[y + cur_drop + 1][x] != 'x':
                        cur_drop += 1
                    else:
                        break
                down_h = min(down_h, cur_drop)
            for y, x in cluster:
                table[y + down_h][x] = 'x'
for line in table:
    print("".join(line))



