# https://www.acmicpc.net/problem/13430
# k에 대한 점화식은 쉽지만 n에 대한 점화식은 행렬을 한 번 써봐야 함
# 이때 추가되는 +1은 더미 행을 둠으로 구현할 수 있다


def dot(matrix1, matrix2):
    r1, c1 = len(matrix1), len(matrix1[0])
    r2, c2 = len(matrix2), len(matrix2[0])
    matrix3 = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] %= 1000000007
    return matrix3


K, N = map(int, input().split())
stack = []
n = N
while n != 1:
    if n % 2 == 0:
        stack.append(True)
        n //= 2
    else:
        stack.append(False)
        n -= 1
init = [[1 if x <= y else 0 for x in range(K + 2)] for y in range(K + 2)]
matrix = [line[:] for line in init]
while stack:
    if stack.pop():
        matrix = dot(matrix, matrix)
    else:
        matrix = dot(init, matrix)
seed = [[0] for _ in range(K + 2)]
seed[0][0] += 1
result = dot(matrix, seed)
print(result[-1][0])