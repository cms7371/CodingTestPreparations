# https://programmers.co.kr/learn/courses/30/lessons/84021
from collections import deque
from functools import reduce
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def points_to_table(points):
    table = [[False] * 6 for _ in range(6)]
    for y, x in arrange_points(points):
        table[y][x] = True
    return table


def arrange_points(points):
    my, mx = reduce(lambda acc, cur: (min(acc[0], cur[0]), min(acc[1], cur[1])), points, (100, 100))
    arr = list(map(lambda p: (p[0] - my, p[1] - mx), points))
    arr.sort()
    return arr


def rotate_points(points):
    return arrange_points(list(map(lambda p: (p[1], -p[0]), points)))


def solution(game_board, table):
    # 테이블에서 조각들을 분리
    N = len(game_board)
    visited = [[False] * N for _ in range(N)]
    blocks = [[] for _ in range(7)]
    for i in range(N):
        for j in range(N):
            if table[i][j] and not visited[i][j]:
                points = [(i, j)]
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                while q:
                    y, x = q.popleft()
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and table[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = True
                            points.append((ny, nx))
                            q.append((ny, nx))
                blocks[len(points)].append(arrange_points(points))
    for i, b in enumerate(blocks):
        print(i)
        for bb in b:
            print(bb)
    # 게임보드에서 빈 공간 찾기
    answer = 0
    for i in range(N):
        for j in range(N):
            if not game_board[i][j]:
                game_board[i][j] = 1
                points = [(i, j)]
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and not game_board[ny][nx]:
                            game_board[ny][nx] = 1
                            points.append((ny, nx))
                            q.append((ny, nx))
                # 빈 공간을 돌려가며 테이블의 조각들과 매칭
                l = len(points)
                points = arrange_points(points)
                print(f"blank in {i}, {j}, shape", *points_to_table(points), sep='\n')
                for _ in range(4):
                    print(f"try {points} shape", *points_to_table(points), sep='\n')
                    if points in blocks[l]:
                        answer += l
                        blocks[l].remove(points)
                        print(f"shape {points} matched")
                        break
                    points = rotate_points(points)
    return answer




print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
