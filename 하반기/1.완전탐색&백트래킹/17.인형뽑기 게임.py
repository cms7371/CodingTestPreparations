# https://programmers.co.kr/learn/courses/30/lessons/64061
# 2019 카카오 인턴십


def solution(board, moves):
    n, m = len(board), len(board[0])
    top = [0] * m
    for i in range(m):
        while top[i] < n and board[top[i]][i] == 0:
            top[i] += 1
    basket = []
    answer = 0
    for m in moves:
        m = m - 1
        if top[m] < n:
            doll = board[top[m]][m]
            top[m] += 1
            if basket and basket[-1] == doll:
                answer += 2
                basket.pop()
            else:
                basket.append(doll)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))