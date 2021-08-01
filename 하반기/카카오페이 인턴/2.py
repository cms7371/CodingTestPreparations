def solution(rows, columns, swipes):
    answer = []
    table = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            table[i][j] = i * columns + j + 1
    for d, y1, x1, y2, x2 in swipes:
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1
        if d == 1:  # 행 번호 증가(아래)
            temp = table[y2][x1:x2 + 1]  # 맨 아래 행 저장
            for i in range(y2 - 1, y1 - 1, -1):  # 아래부터 맨 위까지
                table[i + 1][x1:x2 + 1] = table[i][x1:x2 + 1]  # 아래 행이 윗 행 값으로 갱신(아래로 한칸씩)
            table[y1][x1:x2 + 1] = temp  # 맨 아래 행을 맨 위로
        elif d == 2:  # 행 번호 감소(위)
            temp = table[y1][x1:x2 + 1]  # 맨 윗 행 저장
            for i in range(y1 + 1, y2 + 1):  # 위부터 맨 아래까지
                table[i - 1][x1:x2 + 1] = table[i][x1:x2 + 1]  # 윗 행이 아래 행 값으로 갱신(위로 한칸씩)
            table[y2][x1:x2 + 1] = temp  # 맨 윗 행이 맨 아래로
        elif d == 3:  # 열 번호 증가(오른쪽)
            temp = [table[i][x2] for i in range(y1, y2 + 1)]  # 맨 오른쪽 행 저장
            for x in range(x2 - 1, x1 - 1, -1):  # 오른쪽부터 맨 왼쪽까지
                for y in range(y1, y2 + 1):  # 모든 열에 대해서
                    table[y][x + 1] = table[y][x]  # 한 칸씩 오른쪽으로
            for i in range(y1, y2 + 1):
                table[i][x1] = temp[i - y1]  # 맨 오른 행이 맨 왼쪽으로
        else:  # 행 번호 감소(왼쪽)
            temp = [table[i][x1] for i in range(y1, y2 + 1)]  # 맨 왼쪽 행 저장
            for x in range(x1 + 1, x2 + 1):  # 왼쪽부터 맨 오른쪽까지
                for y in range(y1, y2 + 1):  # 모든 열에 대해서
                    table[y][x - 1] = table[y][x]  # 한 칸씩 왼쪽으로
            for i in range(y1, y2 + 1):
                table[i][x2] = temp[i - y1]
        answer.append(sum(temp))
    return answer


print(solution(4, 3, [[1, 1, 2, 4, 3], [3, 2, 1, 2, 3], [4, 1, 1, 4, 3], [2, 2, 1, 3, 3]]))