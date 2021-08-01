# https://www.acmicpc.net/problem/1018
N, M = map(int, input().split())
table = [input() for _ in range(N)]
result = int(10e9)  # 최종 답과, W로 시작할 때와, B로 시작할 때
for n in range(8, N + 1):
    for m in range(8, M + 1):
        result1, result2 = 0, 0
        for i in range(n - 8, n):
            for j in range(m - 8, m):
                if (i + j) % 2 == 0:  # 짝수일 때
                    if table[i][j] == 'B':
                        result1 += 1
                    else:
                        result2 += 1
                else:
                    if table[i][j] == 'W':
                        result1 += 1
                    else:
                        result2 += 1
        result = min(result, result1, result2)
print(result)