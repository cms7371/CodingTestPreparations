# https://programmers.co.kr/learn/courses/30/lessons/17679
offsets = [(1, 0), (0, 1), (1, 1)]


def solution(m, n, board):
    answer = 0
    board = [list(line) for line in board]
    while True:
        pop_blocks = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != " ":
                    pop_blocks.update(get_square(i, j, board))
        if not pop_blocks:
            break
        answer += len(pop_blocks)
        for y, x in pop_blocks:
            board[y][x] = " "
        new_board = [[" " for _ in range(n)] for _ in range(m)]
        for x in range(n):
            ny = m - 1
            for y in range(m - 1, -1, -1):
                if board[y][x] != " ":
                    new_board[ny][x] = board[y][x]
                    ny -= 1
        board = new_board
        print(*board, "", sep='\n')
    return answer


def get_square(y, x, board):
    cur = board[y][x]
    result = [(y, x)]
    for dy, dx in offsets:
        ny, nx = y + dy, x + dx
        if board[ny][nx] != cur:
            return []
        result.append((ny, nx))
    return result