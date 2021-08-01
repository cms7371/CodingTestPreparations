# https://www.acmicpc.net/problem/1280
# 인덱스가 아닌 거리에 대한 세그먼트 트리를 만들어야함. 각 나무들에 대해 왼쪽에 있는 나무들의 합, 오른쪽에 있는 나무들의 합을 이용해서
# 거리의 합을 구해주고 이를 이용하여 답을 구함
import sys
input = sys.stdin.readline


def update(start, end, node, pos):
    if start <= pos <= end:
        dTree[node] += pos
        nTree[node] += 1
        if start != end:
            mid = (start + end) // 2
            update(start, mid, node * 2 + 1, pos)
            update(mid + 1, end, node * 2 + 2, pos)


def get(start, end, node, left, right):
    if right < start or end < left:
        return 0, 0
    elif left <= start and end <= right:
        return dTree[node], nTree[node]
    else:
        mid = (start + end) // 2
        l_val = get(start, mid, node * 2 + 1, left, right)
        r_val = get(mid + 1, end, node * 2 + 2, left, right)
        return l_val[0] + r_val[0], l_val[1] + r_val[1]


N = int(input())
dTree = [0] * (200001 * 4)
nTree = [0] * (200001 * 4)
result = 1
update(0, 200000, 0, int(input()))
for _ in range(N - 1):
    current = int(input())
    l_dist, l_count = get(0, 200000, 0, 0, current)
    r_dist, r_count = get(0, 200000, 0, current, 200000)
    result *= (current * l_count) - l_dist + r_dist - (current * r_count)
    result %= 1000000007
    update(0, 200000, 0, current)
print(result)