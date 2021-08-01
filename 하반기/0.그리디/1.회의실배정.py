# https://www.acmicpc.net/problem/1931
# 다시 풀어보기
n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]
time = 0
result = 0
meeting.sort(key=lambda x: (x[1], x[0]))
for s, e in meeting:
    if s >= time:
        result += 1
        time = e

print(result)