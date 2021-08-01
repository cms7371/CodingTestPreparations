# https://www.acmicpc.net/problem/14440
def dot(matrix1, matrix2):
    r1, c1 = len(matrix1), len(matrix1[0])
    r2, c2 = len(matrix2), len(matrix2[0])
    matrix3 = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] %= 100
    return matrix3


x, y, a0, a1, N = map(int, input().split())
if N <= 1:
    result = a0 if N == 0 else a1
else:
    init = [[x, y], [1, 0]]
    matrix = [row[:] for row in init]
    n = N - 1
    stack = []
    while n != 1:
        if n % 2 == 0:
            stack.append(True)
            n //= 2
        else:
            stack.append(False)
            n -= 1
    while stack:
        if stack.pop():
            matrix = dot(matrix, matrix)
        else:
            matrix = dot(matrix, init)
    result = dot(matrix, [[a1], [a0]])[0][0]
print("{:02d}".format(result))

