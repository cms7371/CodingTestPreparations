# https://www.acmicpc.net/problem/2357
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
INF = 10 ** 9



def init(start, end, node):
    if start == end:
        tree[node] = (arr[start], arr[start])  # 최소 최대로 저장
    else:
        mid = (start + end) // 2
        l_val, r_val = init(start, mid, node * 2 + 1), init(mid + 1, end, node * 2 + 2)
        tree[node] = (min(l_val[0], r_val[0]), max(l_val[1], r_val[1]))
    return tree[node]


def get_val(start, end, node, left, right):
    if right < start or end < left:
        return INF, 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        l_var, r_val = get_val(start, mid, node * 2 + 1, left, right), get_val(mid + 1, end, node * 2 + 2, left, right)
        return min(l_var[0], r_val[0]), max(l_var[1], r_val[1])


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [tuple()] * (N * 4)
init(0, N - 1, 0)
for _ in range(M):
    a, b = map(int, input().split())
    print(*get_val(0, N - 1, 0, a - 1, b - 1))