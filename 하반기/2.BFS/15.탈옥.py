# https://www.acmicpc.net/problem/9376
from collections import deque


def get_dist(init_pos, dist=None):
    global R, C
    if dist is None:
        dist = [[10 ** 9] * C for _ in range(R)]
    iy, ix = init_pos
    i_val = 1 if table[iy][ix] == '#' else 0
    dist[iy][ix] = i_val
    q = deque()
    q.append((iy, ix, i_val))
    while q:
        y, x, val = q.popleft()
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and table[ny][nx] != '*':
                if table[ny][nx] == '#' and dist[ny][nx] > val + 1:
                    dist[ny][nx] = val + 1
                    q.append((ny, nx, val + 1))
                    n_val = val + 1
                elif (table[ny][nx] == '.' or table[ny][nx] == '$') and dist[ny][nx] > val:
                    dist[ny][nx] = val
                    q.appendleft((ny, nx, val))
    return dist


offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    table = [list(input()) for _ in range(R)]
    c_pos = []
    d_pos = []
    e_pos = []
    for i in range(R):
        for j in range(C):
            if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and table[i][j] != '*':
                e_pos.append((i, j))
            if table[i][j] == '#':
                d_pos.append((i, j))
            elif table[i][j] == '$':
                c_pos.append((i, j))
    # 각 출구로부터 BFS해서 출구로부터 죄수나 문의 최소값을 구함
    escape_val = [[10 ** 9] * C for _ in range(R)]
    for way_out in e_pos:
        get_dist(way_out, escape_val)
    c1, c2 = c_pos
    dist1 = get_dist(c1)
    dist2 = get_dist(c2)

    answer = escape_val[c1[0]][c1[1]] + escape_val[c2[0]][c2[1]]
    for cy, cx in d_pos:
        answer = min(answer, dist1[cy][cx] + dist2[cy][cx] - 2 + escape_val[cy][cx])
    print(answer)

