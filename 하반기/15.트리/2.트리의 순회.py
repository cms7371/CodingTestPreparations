# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(10 ** 9)


def pre_order(in_s, in_e, po_s, po_e):
    if (in_s > in_e) or (po_s > po_e):
        return
    print(post_order[po_e], end=' ')
    mid_offset = pos[post_order[po_e]] - in_s
    pre_order(in_s, in_s + mid_offset - 1, po_s, po_s + mid_offset - 1)
    pre_order(in_s + mid_offset + 1, in_e, po_s + mid_offset, po_e - 1)


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0] * (N + 1)
for i in range(N):
    pos[in_order[i]] = i
pre_order(0, N - 1, 0, N - 1)
