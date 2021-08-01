# 15685번 드래곤 커브 https://www.acmicpc.net/problem/15685
curve_infos = []
offsets = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for _ in range(int(input())):
    curve_infos.append(tuple(map(int, input().split())))
space = [[False] * 101 for _ in range(101)]
for start_x, start_y, direction, generation in curve_infos:
    o = offsets[direction]
    curve = [(start_y, start_x), (start_y + o[0], start_x + o[1])]
    for y, x in curve:
        space[y][x] = True
    for _ in range(generation):
        next_curve = []
        pivot_y, pivot_x = curve[-1]
        for i in range(len(curve) - 2, -1, -1):
            y, x = curve[i]
            dy, dx = y - pivot_y, x - pivot_x
            new_y, new_x = pivot_y + dx, pivot_x - dy
            next_curve.append((new_y, new_x))
        for y, x in next_curve:
            space[y][x] = True
        curve.extend(next_curve)
result = 0
for y in range(100):
    for x in range(100):
        if all((space[y][x], space[y + 1][x], space[y][x + 1], space[y + 1][x + 1])):
            result += 1
print(result)



