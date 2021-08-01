# 15684번 사다리 조작 https://www.acmicpc.net/problem/15684
from itertools import combinations


def explore(graph):
    global n, h
    for start_line in range(n):
        current_line = start_line
        for row in range(h):
            if current_line > 0 and graph[row][current_line - 1] == 1:
                current_line -= 1
            elif current_line < n - 1 and graph[row][current_line] == 1:
                current_line += 1
        if current_line != start_line:
            return False
    return True


n, m, h = map(int, input().split())
original_map = [[0] * (n - 1) for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1  # 가로 0 ~ h - 1까지
    b -= 1  # 세로 0 ~ n - 2까지
    original_map[a][b] = 1
    if b > 0:
        original_map[a][b - 1] = -1
    if b < (n - 2):
        original_map[a][b + 1] = -1
candidates = []
for i in range(h):
    for j in range(n - 1):
        if original_map[i][j] == 0:
            candidates.append((i, j))
added_num = 0
while True:
    if added_num == 0:
        if explore(original_map):
            break
    else:
        cases = combinations(candidates, added_num)
        is_success = False
        for positions in cases:
            current_map = [line[:] for line in original_map]
            skip_case = False
            for x, y in positions:
                if current_map[x][y] == -1:
                    skip_case = True
                    break
                current_map[x][y] = 1
                if y > 0:
                    current_map[x][y - 1] = -1
                if y < n - 2:
                    current_map[x][y + 1] = -1
            if skip_case:  # 진행하면 안되는 케이스에 대해서는 skip
                continue
            if explore(current_map):  # 성공하면 결과로
                is_success = True
                break
        if is_success:
            break
    added_num += 1
    if added_num > 3:  # 3개를 넘어가면 실패 반환
        added_num = -1
        break
print(added_num)