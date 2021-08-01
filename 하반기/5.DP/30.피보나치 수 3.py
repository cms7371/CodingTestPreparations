# https://www.acmicpc.net/problem/2749
def dot(matrix1, matrix2):
    matrix3 = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] %= 1000000
    return matrix3


N = int(input())
if N <= 1:
    result = N
else:
    stack = []
    n = N - 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
            stack.append(True)
        else:
            n -= 1
            stack.append(False)
    init = [[1, 1], [1, 0]]
    result = [[1, 1], [1, 0]]
    while stack:
        if stack.pop():
            result = dot(result, result)
        else:
            result = dot(result, init)
    result = result[0][0]
print(result)




