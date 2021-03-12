# 2828번 사과 담기 게임 https://www.acmicpc.net/problem/2828
n, m = map(int, input().split())
k = int(input())
apples = [int(input()) for _ in range(k)]
current = 1
result = 0
for a in apples:
    if a < current:
        move = current - a
        current -= move
    elif a > current + m - 1:
        move = a - current - m + 1
        current += move
    else:
        continue
    result += move
print(result)

