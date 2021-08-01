# https://www.acmicpc.net/problem/9345
# 최대 최솟값을 리턴하는 세그먼트 트리로 해결해보자 -> 잘못된 생각, max가 더 작아지거나 min이 커지는 것이 반영이 안됨
# -> 아님 반영됨, 영향 받는 노드의 경우 그 아래 영향을 받지 않는 노드와 다시 영향 받는 노드를 통해 갱신되므로 반영됨
import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        min_tree[node], max_tree[node] = start, start
    else:
        mid = (start + end) // 2
        l_val = init(start, mid, node * 2 + 1)
        r_val = init(mid + 1, end, node * 2 + 2)
        min_tree[node] = min(l_val[0], r_val[0])
        max_tree[node] = max(l_val[1], r_val[1])
    return min_tree[node], max_tree[node]


def get(start, end, node, left, right):
    if right < start or end < left:
        return 10 ** 6, -1
    elif left <= start and end <= right:
        return min_tree[node], max_tree[node]
    else:
        mid = (start + end) // 2
        l_val = get(start, mid, node * 2 + 1, left, right)
        r_val = get(mid + 1, end, node * 2 + 2, left, right)
        return min(l_val[0], r_val[0]), max(l_val[1], r_val[1])


def update(start, end, node, idx, val):
    if start <= idx <= end:
        if start == end:
            min_tree[node] = val
            max_tree[node] = val
        else:
            mid = (start + end) // 2
            l_val = update(start, mid, node * 2 + 1, idx, val)
            r_val = update(mid + 1, end, node * 2 + 2, idx, val)
            min_tree[node] = min(l_val[0], r_val[0])
            max_tree[node] = max(l_val[1], r_val[1])
    return min_tree[node], max_tree[node]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    DVD = [i for i in range(N)]
    min_tree = [0] * (N * 4)
    max_tree = [0] * (N * 4)
    init(0, N - 1, 0)
    result = ""
    for _ in range(K):
        q, a, b = map(int, input().split())
        if q == 0:
            update(0, N - 1, 0, a, DVD[b])
            update(0, N - 1, 0, b, DVD[a])
            DVD[a], DVD[b] = DVD[b], DVD[a]
        elif q == 1:
            l, h = get(0, N - 1, 0, a, b)
            result += "YES\n" if a == l and b == h else "NO\n"
    print(result, end='')