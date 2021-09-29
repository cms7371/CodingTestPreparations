# https://programmers.co.kr/learn/courses/30/lessons/42892
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)


def solution(nodeinfo):
    N = len(nodeinfo)
    y_to_nodes = defaultdict(list)
    level_to_y = set()
    for num, node in enumerate(nodeinfo):
        x, y = node
        level_to_y.add(y)
        y_to_nodes[y].append((num + 1, x))
    level_to_y = list(level_to_y)
    level_to_y.sort(reverse=True)
    tree = [None] * (N + 1)
    print(level_to_y)
    print(y_to_nodes)

    def explore(node_idx, level, left, right, mid):
        if level == len(level_to_y) - 1:
            tree[node_idx] = (0, 0)
            return
        child_y = level_to_y[level + 1]
        candidates = y_to_nodes[child_y]
        # 왼쪽 자식 찾기
        left_c = 0
        for n, nx in candidates:
            if left < nx < mid:
                left_c = n
                explore(n, level + 1, left, mid, nx)
                break
        right_c = 0
        for n, nx in candidates:
            if mid < nx < right:
                right_c = n
                explore(n, level + 1, mid, right, nx)
                break
        tree[node_idx] = (left_c, right_c)

    root, root_x = y_to_nodes[level_to_y[0]][0]
    explore(root, 0, -1, 100001, root_x)
    print(tree)

    def pre_order(n, result):
        result.append(n)
        lc, rc = tree[n]
        if lc:
            pre_order(lc, result)
        if rc:
            pre_order(rc, result)
        return result

    def post_order(n, result):
        lc, rc = tree[n]
        if lc:
            post_order(lc, result)
        if rc:
            post_order(rc, result)
        result.append(n)
        return result
    answer = [pre_order(root, []), post_order(root, [])]
    assert len(answer[0]) == N and len(answer[1]) == N
    return answer
