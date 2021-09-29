# https://www.acmicpc.net/problem/4991
from collections import deque
import sys
from itertools import permutations
INF = 10 ** 9
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
input = sys.stdin.readline


def solve(graph, N, M):
    trash = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '*':
                trash.append((i, j))
            elif graph[i][j] == 'o':
                trash.appendleft((i, j))
    trash = list(trash)
    L = len(trash)
    dist = [[INF] * L for _ in range(L)]
    pos_to_idx = {trash[i]: i for i in range(len(trash))}
    for i in range(len(trash)):
        sy, sx = trash[i]
        visited = [[False] * M for _ in range(N)]
        visited[sy][sx] = True
        q = deque()
        q.append((sy, sx, 0))
        while q:
            y, x, d = q.popleft()
            for dy, dx in offsets:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] != 'x':
                    visited[ny][nx] = True
                    q.append((ny, nx, d + 1))
                    if graph[ny][nx] == '*':
                        other = pos_to_idx[(ny, nx)]
                        if dist[i][other] == INF:
                            dist[i][other] = d + 1
                            dist[other][i] = d + 1
        if i == 0:
            for j in range(1, L):
                if dist[i][j] == INF:
                    return -1
    result = INF
    case = permutations(range(1, L), L - 1)
    for seq in case:
        cur = 0
        local_result = 0
        for node in seq:
            local_result += dist[cur][node]
            cur = node
        result = min(result, local_result)
    # bit masking 을 이용한 방법
    # q = deque()
    # q.append((0, 0, 1))
    # while q:
    #     cur, d, mask = q.popleft()
    #     if mask == (2 ** L - 1):
    #         result = min(result, d)
    #         continue
    #     for _next in range(L):
    #         n_bit = (2 ** _next)
    #         if not (n_bit & mask):
    #             n_mask = mask | n_bit
    #             q.append((_next, d + dist[cur][_next], n_mask))
    return result




while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break
    table = [list(input()) for _ in range(R)]
    print(solve(table, R, C))