# https://www.acmicpc.net/problem/14289
import sys
input = sys.stdin.readline


def dot(matrix1, matrix2):
    matrix3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] %= 1000000007
    return matrix3


N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    graph[s][e] = 1
    graph[e][s] = 1
stack = []
n = int(input())
while n != 1:
    if n % 2 == 0:
        n //= 2
        stack.append(True)
    else:
        n -= 1
        stack.append(False)
result = [line[:] for line in graph]
while stack:
    if stack.pop():
        result = dot(result, result)
    else:
        result = dot(result, graph)
print(result[0][0])