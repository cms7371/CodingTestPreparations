# https://www.acmicpc.net/problem/10830
# 빠른 거듭 제곱 방법: N의 B 제곱을 구할 때 B번 하는게 아닌 제곱의 제곱으로 접근
import sys
input = sys.stdin.readline


def dot(matrix1, matrix2):
    matrix3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] %= 1000
    return matrix3


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
pow_stack = []
while B != 1:
    if B % 2 == 0:  # 짝수이면
        B //= 2
        pow_stack.append(True)
    else:
        B -= 1
        pow_stack.append(False)
result = [line[:] for line in matrix]
while pow_stack:
    if pow_stack.pop():
        result = dot(result, result)
    else:
        result = dot(result, matrix)
for row in result:
    print(*row)
