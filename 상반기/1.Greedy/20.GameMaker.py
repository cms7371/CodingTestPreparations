# 2847번 게임을 만든 동준 https://www.acmicpc.net/problem/2847
# 복습 풀이
n = int(input())
levels = [int(input()) for _ in range(n)]
result = 0
for i in range(n-2, -1, -1):
    if levels[i] >= levels[i + 1]:
        result += levels[i] - levels[i + 1] + 1
        levels[i] = levels[i + 1] - 1
print(result)

# 첫 풀이
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

