# https://www.acmicpc.net/problem/8972
from collections import defaultdict

offsets = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]


def plus(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def dist(tuple1, tuple2):
    return abs(tuple1[0] - tuple2[0]), abs(tuple1[1] - tuple2[1])


R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]
command = list(map(lambda x: int(x) - 1, list(input())))
enemy = set()
JongSu = (0, 0)
for i in range(R):
    for j in range(C):
        if table[i][j] == 'I':
            JongSu = (i, j)
        elif table[i][j] == 'R':
            enemy.add((i, j))
time = 0
while time < len(command):
    cmd = command[time]
    JongSu = plus(JongSu, offsets[cmd])
    if JongSu in enemy:
        break
    next_enemy = defaultdict(int)
    for pos in enemy:
        n_pos = plus(pos, sorted(offsets, key=lambda x: dist(JongSu, plus(pos, x)))[0])
        next_enemy[n_pos] += 1
    if JongSu in next_enemy:
        break
    enemy = set(key for key, val in next_enemy.items() if val == 1)
    time += 1
if time == len(command):
    table = [['.'] * C for _ in range(R)]
    table[JongSu[0]][JongSu[1]] = 'I'
    for pos in enemy:
        table[pos[0]][pos[1]] = 'R'
    for line in table:
        print(''.join(line))
else:
    print(f"kraj {time + 1}")
