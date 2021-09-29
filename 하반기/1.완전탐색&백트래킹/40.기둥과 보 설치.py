# https://programmers.co.kr/learn/courses/30/lessons/60061
offsets = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]


# 기둥은 1, 보는 2로 비트마스킹
def solution(n, build_frame):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y, is_beam, is_install in build_frame:
        if is_install:
            assert not table[y][x] & (2 if is_beam else 1)
        if is_install and is_valid(y, x, is_beam, table, n):
            if is_beam:
                table[y][x] |= 2
            else:
                table[y][x] |= 1
        elif not is_install:
            assert table[y][x] & (2 if is_beam else 1)
            table[y][x] ^= 2 if is_beam else 1
            affected_structures = get_adjacent_pos(y, x, table, n)
            if not all(map(lambda a: is_valid(*a, table, n), affected_structures)):
                table[y][x] ^= 2 if is_beam else 1
        print(f"cur oper {y}, {x}, {is_beam}, {is_install}")
        print(*table, sep='\n')
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if table[y][x] & 1:
                answer.append([x, y, 0])
            if table[y][x] & 2:
                answer.append([x, y, 1])
    return answer


def is_valid(y, x, is_beam, table, n):
    if is_beam:
        if table[y - 1][x] & 1 or (x < n and table[y - 1][x + 1] & 1):
            return True
        elif (0 < x < n - 1) and table[y][x - 1] & 2 and table[y][x + 1] & 2:
            return True
        else:
            return False
    else:
        # 바닥에 붙어 있는 경우
        if y == 0:
            return True
        else:
            # 기둥 위나 보 바로 위에 있거나 보의 오른 편에 있는 경우
            if table[y - 1][x] & 1 or (x > 0 and (table[y][x - 1] & 2 or table[y][x] & 2)):
                return True
            else:
                return False


def get_adjacent_pos(y, x, table, n):
    result = []
    for dy, dx in offsets:
        ny, nx = y + dy, x + dx
        if 0 <= ny <= n and 0 <= nx <= n and table[ny][nx]:
            if table[ny][nx] & 1:
                result.append((ny, nx, 0))
            if table[ny][nx] & 2:
                result.append((ny, nx, 1))
    return result


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
