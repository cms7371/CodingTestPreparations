# https://www.acmicpc.net/problem/3653
# 펜윅 트리를 이용한 풀이, 세그먼트는 아슬아슬 아찔함
# 추가 -> 방향을 뒤집으면 get을 두 번 할 필요가 없어서 더 빨리 가능


def update(idx, diff):
    global N, M
    while idx <= N + M:
        tree[idx] += diff
        idx += (idx & - idx)


def get(idx):
    out = 0
    while idx > 0:
        out += tree[idx]
        idx -= (idx & -idx)
    return out


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    query = map(int, input().split())
    tree = [0] * (N + M + 1)  # 0은 사용하지 않고 1에서 N + M까지 사용
    pos = [n for n in range(N + 1, 0, -1)]  # 1번이 N에 위치, N번이 1에 위치
    for i in range(1, N + 1):
        update(i, 1)
    for i, q in enumerate(query):
        n_pos = N + i + 1
        c_pos = pos[q]
        print(get(n_pos) - get(c_pos), end=' ')
        pos[q] = n_pos
        update(n_pos, 1)
        update(c_pos, -1)
    print("")






# 세그먼트 트리가 맨위(i)에서 DVD까지의 개수를 리턴하도록 만들기
import sys
input = sys.stdin.readline


def init(start, end, node, n):
    if start == end:
        if start < n:
            seg_tree[node] = 1
    elif start >= N:
        return 0
    else:
        mid = (start + end) // 2
        seg_tree[node] = init(start, mid, node * 2 + 1, n) + init(mid + 1, end, node * 2 + 2, n)
    return seg_tree[node]


def update(start, end, node, del_node, new_node):
    if start <= del_node <= end or start <= new_node <= end:
        if start <= del_node <= end:
            seg_tree[node] -= 1
        if start <= new_node <= end:
            seg_tree[node] += 1
        if start != end:
            mid = (start + end) // 2
            update(start, mid, node * 2 + 1, del_node, new_node)
            update(mid + 1, end, node * 2 + 2, del_node, new_node)


def get(start, end, node, left, right):
    if right < start or end < left:
        return 0
    elif left <= start and end <= right:
        return seg_tree[node]
    else:
        mid = (start + end) // 2
        return get(start, mid, node * 2 + 1, left, right) + get(mid + 1, end, node * 2 + 2, left, right)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    query = map(int, input().split())
    pos = [n for n in range(N, -1, -1)]  # 1번이 n - 1에 위치 n번이 0에 위치
    result = []
    seg_tree = [0] * ((N + M) * 4)
    init(0, N + M - 1, 0, N)
    for i, q in enumerate(query):
        n_pos = N + i
        c_pos = pos[q]
        result.append(get(0, N + M - 1, 0, c_pos, n_pos) - 1)
        update(0, N + M - 1, 0, c_pos, n_pos)
        pos[q] = n_pos
    print(*result)


