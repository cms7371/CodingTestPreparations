# https://programmers.co.kr/learn/courses/30/lessons/42894
from collections import deque
from functools import reduce

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(board):
    N = len(board)
    block_dict = {}
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] and not visited[i][j]:
                cur_num = board[i][j]
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                cur_points = [(i, j)]
                while q:
                    y, x = q.popleft()
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == cur_num and not visited[ny][nx]:
                            visited[ny][nx] = True
                            cur_points.append((ny, nx))
                            q.append((ny, nx))
                cur_blanks = []
                y1, x1, y2, x2 = reduce(
                    lambda a, c: (min(a[0], c[0]), min(a[1], c[1]), max(a[2], c[0]), max(a[3], c[1])),
                    cur_points, (N, N, 0, 0))
                print(y1, x1, y2, x2)
                for y in range(y1, y2 + 1):
                    for x in range(x1, x2 + 1):
                        if (y, x) not in cur_points:
                            cur_blanks.append((y, x))
                print(f"num = {cur_num}, points = {cur_points}, blanks = {cur_blanks}")
                block_dict[cur_num] = [cur_points, cur_blanks]

    def is_removable(n):
        block_points, block_blanks = block_dict[n]
        for cy, cx in block_blanks:
            if board[cy][cx] or any([board[uy][cx] for uy in range(0, cy)]):
                return False
        for cy, cx in block_points:
            board[cy][cx] = 0
        del block_dict[n]
        return True

    is_updated = True
    result = 0
    while is_updated and block_dict:
        is_updated = False
        for num in list(block_dict.keys()):
            if is_removable(num):
                result += 1
                is_updated = True
    return result

    # answer = 0
    # i = 0
    # while i < N:
    #     j = 0
    #     while j < N:
    #         if board[i][j]:
    #             if is_removable(board[i][j]):
    #                 answer += 1
    #                 i = -1
    #             break
    #         else:
    #             j += 1
    #     i += 1
    # return answer


print(solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]))
