from collections import deque, defaultdict

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def find(p, a):
    if p[a] != a:
        p[a] = find(p, p[a])
    return p[a]


def union(p, a, b):
    if a < b:
        p[find(p, b)] = find(p, a)
    else:
        p[find(p, a)] = find(p, b)


def solution(land, height):
    n = len(land)
    num_table = [[-1] * n for _ in range(n)]
    cur_num = 0
    diff_dict = defaultdict(lambda: 10001)
    for i in range(n):
        for j in range(n):
            if num_table[i][j] == -1:
                num_table[i][j] = cur_num
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n:
                            if num_table[ny][nx] == -1:
                                if abs(land[ny][nx] - land[y][x]) <= height:
                                    num_table[ny][nx] = cur_num
                                    q.append((ny, nx))
                            elif num_table[ny][nx] != cur_num:
                                other_num = num_table[ny][nx]
                                key = (other_num, cur_num)
                                diff = abs(land[ny][nx] - land[y][x])
                                diff_dict[key] = min(diff_dict[key], diff)
                cur_num += 1
    parent = list(range(cur_num))
    diff_list = [(val, *key) for key, val in diff_dict.items()]
    diff_list.sort(reverse=True)
    count = 0
    result = 0
    while diff_list and any(parent):
        diff, l1, l2 = diff_list.pop()
        if find(parent, l1) != find(parent, l2):
            result += diff
            union(parent, l1, l2)
            count += 1
    return result


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
