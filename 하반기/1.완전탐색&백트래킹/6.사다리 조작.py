# https://www.acmicpc.net/problem/15684
from itertools import combinations


def explore(l_positions):
    global n, h
    for start_i in range(n):
        cnt_i = start_i
        for cnt_h in range(h):
            if cnt_i < n - 1 and l_positions[cnt_h][cnt_i] == 1:
                cnt_i += 1
            elif cnt_i > 0 and l_positions[cnt_h][cnt_i - 1] == 1:
                cnt_i -= 1
        if cnt_i != start_i:
            return False
    return True


n, m, h = map(int, input().split())
ladder_positions = [[0] * (n - 1) for _ in range(h)]
for _ in range(m):
    y, x = map(int, input().split())
    x -= 1  # 좌표 보정 x는 i번째와 i+1번째 사이이며 i <= n - 1
    y -= 1
    ladder_positions[y][x] = 1
    if x > 0:
        ladder_positions[y][x - 1] = -1
    if x < n - 2:
        ladder_positions[y][x + 1] = -1
blank_positions = []
for y in range(h):
    for x in range(n - 1):
        if ladder_positions[y][x] == 0:
            blank_positions.append((y, x))
result = 0
while True:
    if result > 3:
        result = -1
        break
    elif result == 0 and explore(ladder_positions):
        break
    else:
        combs = combinations(blank_positions, result)
        is_possible = False
        for ladders in combs:
            is_continue = False  # 새로 추가되는 다리가 연속되는 경우 검출
            for i in range(result - 1):
                if is_continue:
                    break
                for j in range(1, result):
                    if ladders[i][0] == ladders[j][0] and abs(ladders[i][1] - ladders[j][1]) == 1:
                        is_continue = True
                        break
            if is_continue:
                continue
            # 아니라면 테스트함
            cnt_ladder_positions = [line[:] for line in ladder_positions]
            for y, x in ladders:
                cnt_ladder_positions[y][x] = 1
            if explore(cnt_ladder_positions):
                is_possible = True
                break
        if is_possible:
            break
        else:
            result += 1
print(result)
