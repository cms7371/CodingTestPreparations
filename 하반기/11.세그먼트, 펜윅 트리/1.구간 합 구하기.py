# https://www.acmicpc.net/problem/2042
import sys
input = sys.stdin.readline


def init_seg(start, end, node):
    if start == end:
        segment_tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        segment_tree[node] = init_seg(start, mid, node * 2 + 1) + init_seg(mid + 1, end, node * 2 + 2)
    return segment_tree[node]


def seg_sum(start, end, left, right, node):
    if start > right or end < left:
        return 0
    elif left <= start and end <= right:
        return segment_tree[node]
    else:
        mid = (start + end) // 2
        return seg_sum(start, mid, left, right, node * 2 + 1) + seg_sum(mid + 1, end, left, right, node * 2 + 2)


def seg_update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    else:
        segment_tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            seg_update(start, mid, node * 2 + 1, idx, diff)
            seg_update(mid + 1, end, node * 2 + 2, idx, diff)


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
segment_tree = [0] * (N * 4)
init_seg(0, N - 1, 0)
for _ in range(M + K):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        seg_update(0, N - 1, 0, a - 1, b - arr[a - 1])
        arr[a - 1] = b
    else:
        print(seg_sum(0, N - 1, a - 1, b - 1, 0))