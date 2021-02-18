# 2217번 로프 https://www.acmicpc.net/problem/2217
n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
result = 0
for i in range(n):
    result = max(result, ropes[i] * (n - i))
print(result)
