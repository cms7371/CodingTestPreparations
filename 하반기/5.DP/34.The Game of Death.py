# https://www.acmicpc.net/problem/2099
import sys
input = sys.stdin.readline


def dot(matrix1, matrix2):
    r1, c1 = len(matrix1), len(matrix1[0])
    r2, c2 = len(matrix2), len(matrix2[0])
    matrix3 = [[False] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                matrix3[i][j] |= matrix1[i][k] & matrix2[k][j]
                if matrix3[i][j]:
                    break
    return matrix3


N, K, M = map(int, input().split())
init = [[False] * N for _ in range(N)]
for s in range(N):
    e1, e2 = map(int, input().split())
    init[s][e1 - 1] = True
    init[s][e2 - 1] = True
case = []
for _ in range(M):
    s, e = map(int, input().split())
    case.append((s - 1, e - 1))
matrix = [row[:] for row in init]
stack = []
k = K
while k != 1:
    if k % 2 == 0:
        stack.append(True)
        k //= 2
    else:
        stack.append(False)
        k -= 1
while stack:
    if stack.pop():
        matrix = dot(matrix, matrix)
    else:
        matrix = dot(matrix, init)
for s, e in case:
    print("death" if matrix[s][e] else "life")