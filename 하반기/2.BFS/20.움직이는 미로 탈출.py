# https://www.acmicpc.net/problem/16954
offsets = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]


def solve():
    table = [list(input()) for _ in range(8)]
    wall_pos = set()
    for i in range(8):
        for j in range(8):
            if table[i][j] == '#':
                wall_pos.add((i, j))
    pos = [(7, 0)]
    while pos:
        next_pos = []
        visited = [[False] * 8 for _ in range(8)]
        for y, x in pos:
            if y == 0 and x == 7:
                return 1
            if (y, x) in wall_pos:
                continue
            for dy, dx in offsets:
                ny, nx = y + dy, x + dx
                if 0 <= ny < 8 and 0 <= nx < 8 and not visited[ny][nx] and (ny, nx) not in wall_pos:
                    visited[ny][nx] = True
                    next_pos.append((ny, nx))
        pos = next_pos
        wall_pos = [(p[0] + 1, p[1]) for p in wall_pos if p[0] < 7]
    return 0


print(solve())

