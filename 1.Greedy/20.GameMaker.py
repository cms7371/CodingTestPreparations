# 2847번 게임을 만든 동준 https://www.acmicpc.net/problem/2847
n = int(input())
game = [int(input()) for _ in range(n)]
result = 0
current = game.pop()
while game:
    g = game.pop()
    if g < current:
        current = g
        continue
    else:
        result += g - current + 1
        current -= 1
print(result)

