# https://www.acmicpc.net/problem/9341
# 점화식 세우기 매우 어려웠음...
# ZZ(i,k) = ZZ(0, k-2) + ZZ(0, k-1) + ZZ(1, k-1) ... ZZ(i, k-1)임을 이용
import sys
input = sys.stdin.readline



def dot(matrix1, matrix2):
    r1, c1 = len(matrix1), len(matrix1[0])
    r2, c2 = len(matrix2), len(matrix2[0])
    matrix3 = [[0] * c2 for _ in range(r1)]
    for m1row in range(r1):
        for m2col in range(c2):
            for intersection in range(c1):
                matrix3[m1row][m2col] += matrix1[m1row][intersection] * matrix2[intersection][m2col]
            matrix3[m1row][m2col] %= 1000000009
    return matrix3


T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if d == 1:
        print(a)
    elif d == 2:
        print(c * a + b)
    else:
        m_size = c + 2
        init_matrix = [[0] * m_size for _ in range(m_size)]
        for i in range(m_size):
            for j in range(m_size):
                if i >= j:
                    init_matrix[i][j] = 1
        init_matrix[0][0:2] = [0, 1]
        goal = d - 2
        stack = []
        while goal != 1:
            if goal % 2 == 0:
                stack.append(True)
                goal //= 2
            else:
                stack.append(False)
                goal -= 1
        result_matrix = [line[:] for line in init_matrix]
        while stack:
            if stack.pop():
                result_matrix = dot(result_matrix, result_matrix)
            else:
                result_matrix = dot(result_matrix, init_matrix)
        seed = [[a]]
        for i in range(c + 1):
            seed.append([a * i + b])
        result = dot(result_matrix, seed)
        print(result[c + 1][0])





