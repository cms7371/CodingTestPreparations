# https://www.acmicpc.net/problem/5213
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def num_to_rc(num):
    global N
    num -= 1
    row = num // (2 * N - 1) * 2
    remain = num % (2 * N - 1)
    if remain >= N:
        row += 1
        col = remain - N
    else:
        col = remain
    return row, col


def rc_to_num(row, col):
    global N
    num = (row // 2) * (2 * N - 1) + col + 1
    if row % 2:
        num += N
    return num


def track_back(num):
    prev = visited[num][0]
    if prev != num:
        track_back(prev)
    print(num, end=" ")


N = int(input())
tile = [(0, 0)]
for _ in range(N ** 2 - N // 2):
    tile.append(tuple(map(int, input().split())))
visited = [None] * (N ** 2 - N // 2 + 1)
q = deque()
q.append((1, 1))
visited[1] = (1, 1)
while q:
    cur, dist = q.popleft()
    r, c = num_to_rc(cur)
    cur_tile = tile[cur]
    # 짝수항(0, 2, 4)에서
    next_tiles = []
    if r % 2 == 0:
        if c < N - 1:
            right_tiles = [rc_to_num(r, c + 1)]
            if r > 0:
                right_tiles.append(rc_to_num(r - 1, c))
            if r < N - 1:
                right_tiles.append(rc_to_num(r + 1, c))
            for right in right_tiles:
                if cur_tile[1] == tile[right][0] and not visited[right]:
                    next_tiles.append(right)
        if c > 0:
            left_tiles = [rc_to_num(r, c - 1)]
            if r > 0:
                left_tiles.append(rc_to_num(r - 1, c - 1))
            if r < N - 1:
                left_tiles.append(rc_to_num(r + 1, c - 1))
            for left in left_tiles:
                if cur_tile[0] == tile[left][1] and not visited[left]:
                    next_tiles.append(left)
    else:
        right_tiles = [rc_to_num(r - 1, c + 1)]
        left_tiles = [rc_to_num(r - 1, c)]
        if c < N - 2:
            right_tiles.append(rc_to_num(r, c + 1))
        if c > 0:
            left_tiles.append(rc_to_num(r, c - 1))
        if r < N - 1:
            left_tiles.append(rc_to_num(r + 1, c))
            right_tiles.append(rc_to_num(r + 1, c + 1))
        for left in left_tiles:
            if cur_tile[0] == tile[left][1] and not visited[left]:
                next_tiles.append(left)
        for right in right_tiles:
            if cur_tile[1] == tile[right][0] and not visited[right]:
                next_tiles.append(right)
    for _next in next_tiles:
        visited[_next] = (cur, dist + 1)
        q.append((_next, dist + 1))
answer = 1
for i in range(N ** 2 - N // 2, 0, -1):
    if visited[i]:
        answer = i
        break

print(visited[answer][1])
track_back(answer)