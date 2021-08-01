# 14891번 톱니바퀴 https://www.acmicpc.net/problem/14891
gears = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())
moves = [tuple(map(int, input().split())) for _ in range(k)]
for idx, d in moves:
    idx -= 1
    is_coupled = [gears[i][2] != gears[i + 1][6] for i in range(3)]
    rotations = [0] * 4
    rotations[idx] = d
    for i in range(idx, 3):
        if rotations[i] != 0 and is_coupled[i]:
            rotations[i + 1] = -1 if rotations[i] == 1 else 1
    for i in range(idx, 0, -1):
        if rotations[i] != 0 and is_coupled[i - 1]:
            rotations[i - 1] = -1 if rotations[i] == 1 else 1
    for i in range(4):
        if rotations[i] == 1:
            gears[i] = [gears[i][7]] + gears[i][:7]
        elif rotations[i] == -1:
            gears[i] = gears[i][1:] + [gears[i][0]]
print(sum([pow(2, i) for i in range(4) if gears[i][0]]))

