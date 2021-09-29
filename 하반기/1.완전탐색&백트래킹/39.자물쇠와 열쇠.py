# https://programmers.co.kr/learn/courses/30/lessons/60059
from functools import reduce


def solution(key, lock):
    K, L = len(key), len(lock)
    key_points = table_to_points(key)
    lock_points = table_to_points(lock, True)
    lock_points.sort()
    if not lock_points:
        return True
    print(f"lock points = {lock_points}")
    for _ in range(4):
        for dy in range(-K + 1, L):
            for dx in range(-K + 1, L):
                cur_key_points = slide_points(key_points, dy, dx, L)
                cur_key_points.sort()
                print(f"cur_key_points = {cur_key_points}")
                if cur_key_points and cur_key_points == lock_points:
                    return True
        key_points = arrange_points(rotate_points(key_points))
    return False


def table_to_points(table, isLock=False):
    R, C = len(table), len(table[0])
    points = []
    for i in range(R):
        for j in range(C):
            if (isLock and not table[i][j]) or not isLock and table[i][j]:
                points.append((i, j))
    return points


def arrange_points(points):
    min_y, min_x = reduce(lambda acc, cur: (min(cur[0], acc[0]), min(cur[1], acc[1])), points, (100, 100))
    return list(map(lambda p: (p[0] - min_y, p[1] - min_x), points))


def rotate_points(points):
    return list(map(lambda p: (p[1], -p[0]), points))


def slide_points(points, dy, dx, limit):
    return list(
        filter(lambda p: (0 <= p[0] < limit and 0 <= p[1] < limit),
               map(lambda p: (p[0] + dy, p[1] + dx),
                   points)))


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
