# https://www.acmicpc.net/problem/2931

def explore(pos):
    y, x = pos
    d = -1
    global R, C
    while True:
        # 남쪽으로 흐를 때
        if y < R - 1 and (d == 0 or d == -1):
            if table[y + 1][x] != '.' and table[y + 1][x] in nd_dict[0]:
                visited[y + 1][x] = True
                d = nd_dict[0][table[y + 1][x]]
                y += 1
                continue
        if x < C - 1 and (d == 1 or d == -1):
            if table[y][x + 1] != '.' and table[y][x + 1] in nd_dict[1]:
                visited[y][x + 1] = True
                d = nd_dict[1][table[y][x + 1]]
                x += 1
                continue
        if y > 0 and (d == 2 or d == -1):
            if table[y - 1][x] != '.' and table[y - 1][x] in nd_dict[2]:
                visited[y - 1][x] = True
                d = nd_dict[2][table[y - 1][x]]
                y -= 1
                continue
        if x > 0 and (d == 3 or d == -1):
            if table[y][x - 1] != '.' and table[y][x - 1] in nd_dict[3]:
                visited[y][x - 1] = True
                d = nd_dict[3][table[y][x - 1]]
                x -= 1
                continue
        return y, x, d


def get_answer(end_p):
    ay, ax, ad = end_p[0]
    ay, ax = ay + offsets[ad][0], ax + offsets[ad][1]
    global R, C
    for dy, dx in offsets:
        ny, nx = ay + dy, ax + dx
        if 0 <= ny < R and 0 <= nx < C and table[ny][nx] not in ('.', 'M', 'Z') and not visited[ny][nx]:
            return ay + 1, ax + 1, '+'
    directions = {(end_p[0][2] + 2) % 4, (end_p[1][2] + 2) % 4}
    if directions == {0, 2}:
        shape = '|'
    elif directions == {1, 3}:
        shape = '-'
    elif directions == {0, 1}:
        shape = '1'
    elif directions == {1, 2}:
        shape = '2'
    elif directions == {2, 3}:
        shape = '3'
    else:
        shape = '4'
    return ay + 1, ax + 1, shape





offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 남 동, 북, 서 순서
nd_dict = {0: {'|': 0, '+': 0, '2': 1, '3': 3},
           1: {'-': 1, '+': 1, '3': 2, '4': 0},
           2: {'|': 2, '+': 2, '1': 1, '4': 3},
           3: {'-': 3, '+': 3, '1': 0, '2': 2}}
R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]
init_pos = []
for i in range(R):
    for j in range(C):
        if table[i][j] == 'M' or table[i][j] == 'Z':
            init_pos.append((i, j))
visited = [[False] * C for _ in range(R)]
end_pos = [explore(p) for p in init_pos]
print(*get_answer(end_pos))
