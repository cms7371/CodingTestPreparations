# 13460번 구슬 탈출 2 https://www.acmicpc.net/problem/13460
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move(rx, ry, bx, by, moves, direct):
    dx, dy = directions[direct]
    nrx, nry, nbx, nby = rx, ry, bx, by
    while True:
        if (rx + dx, ry + dy) == out or (rx, ry) == out:
            nrx, nry = out
        elif graph[rx + dx][ry + dy] == 0 and (rx + dx, ry + dy) != (bx, by):
            nrx, nry = rx + dx, ry + dy
        if (bx + dx, by + dy) == out or (bx, by) == out:
            nbx, nby = out
        elif graph[bx + dx][by + dy] == 0 and (bx + dx, by + dy) != (rx, ry):
            nbx, nby = bx + dx, by + dy
        if (rx, ry) == (nrx, nry) and (bx, by) == (nbx, nby):
            return rx, ry, bx, by, moves + 1, direct
        else:
            rx, ry, bx, by = nrx, nry, nbx, nby


n, m = map(int, input().split())
original = [list(input()) for _ in range(n)]
graph = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if original[i][j] == "#":
            graph[i][j] = 1
        elif original[i][j] == "R":
            red = (i, j)
        elif original[i][j] == "B":
            blue = (i, j)
        elif original[i][j] == "O":
            out = (i, j)
q = deque()
q.append((*red, *blue, 0, None))
output = -1
stop = False
while q and not stop:
    r1, r2, b1, b2, cnt, direction = q.popleft()
    for i in range(4):
        if i != direction:
            result = move(r1, r2, b1, b2, cnt, i)
            if result[2:4] == out:
                continue
            elif result[0:2] == out:
                output = result[4]
                stop = True
                break
            elif result[4] < 10 and result[:4] != (r1, r2, b1, b2):
                q.append(result)
print(output)