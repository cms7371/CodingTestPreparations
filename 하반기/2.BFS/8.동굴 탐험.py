# https://programmers.co.kr/learn/courses/30/lessons/67260
# 2020 카카오 인턴십
from collections import deque


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for p, c in path:
        graph[p].append(c)
        graph[c].append(p)
    tree = [[] for _ in range(n)]
    q = deque()
    q.append((0, -1))
    while q:
        now, parent = q.popleft()
        for child in graph[now]:
            if child != parent:
                tree[now].append(child)
                q.append((child, now))
    before = dict()
    after = set()
    for p, a in order:
        before[p] = a
        after.add(a)
    knocked = [False] * n
    v_num = 0
    q = deque()
    if 0 in before:
        after.remove(before[0])
    if 0 not in after:
        q.append(0)
    while q:
        v_num += 1
        now = q.popleft()
        for c in tree[now]:
            if c in before:
                q.append(c)
                if knocked[before[c]]:
                    q.append(before[c])
                else:
                    after.remove(before[c])
            elif c in after:
                knocked[c] = True
            else:
                q.append(c)
    if v_num == n:
        return True
    else:
        return False


print(solution(3, [[0, 1], [0, 2]], [[1, 2]]))