# https://www.acmicpc.net/problem/11505
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
MOD = 1000000007


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node * 2 + 1) * init(mid + 1, end, node * 2 + 2) % MOD
    return tree[node]


def get_mul(start, end, node, left, right):
    if right < start or end < left:
        return 1
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return get_mul(start, mid, node * 2 + 1, left, right) * get_mul(mid + 1, end, node * 2 + 2, left, right) % MOD


def update_node(start, end, node, idx, val):
    if start == end and start == idx:
        tree[node] = val
    elif start <= idx <= end:
        mid = (start + end) // 2
        tree[node] = update_node(start, mid, node * 2 + 1, idx, val) * update_node(mid + 1, end, node * 2 + 2, idx, val) % MOD
    return tree[node]


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)
init(0, N - 1, 0)
for _ in range(M + K):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        update_node(0, N - 1, 0, a - 1, b)
    elif cmd == 2:
        print(get_mul(0, N - 1, 0, a - 1, b - 1))
