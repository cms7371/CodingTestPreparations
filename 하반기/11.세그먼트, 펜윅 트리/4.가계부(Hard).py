# https://www.acmicpc.net/problem/12837
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def get(start, end, node, left, right):
    if right < start or end < left:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return get(start, mid, node * 2 + 1, left, right) + get(mid + 1, end, node * 2 + 2, left, right)


def update(start, end, node, day, val):
    if start <= day <= end:
        tree[node] += val
        if start != end:
            mid = (start + end) // 2
            update(start, mid, node * 2 + 1, day, val)
            update(mid + 1, end, node * 2 + 2, day, val)


N, Q = map(int, input().split())
tree = [0] * (N * 4)
for _ in range(Q):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        update(1, N, 0, a, b)
    elif cmd == 2:
        print(get(1, N, 0, a, b))
