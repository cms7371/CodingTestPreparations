# https://www.acmicpc.net/problem/3020
import sys
input = sys.stdin.readline
n, h = map(int, input().split())
lower_pillar = [0] * h
upper_pillar = [0] * h
switch = False
for _ in range(n):
    if switch:
        switch = False
        upper_pillar[int(input()) - 1] += 1
    else:
        switch = True
        lower_pillar[int(input()) - 1] += 1
for i in range(h - 2, -1, -1):
    lower_pillar[i] += lower_pillar[i + 1]
    upper_pillar[i] += upper_pillar[i + 1]
for i in range(h):
    lower_pillar[i] += upper_pillar[-1 - i]
min_val = 10e9
num = 0
for obstacles in lower_pillar:
    if obstacles < min_val:
        num = 1
        min_val = obstacles
    elif obstacles == min_val:
        num += 1
print(min_val, num)

# 더 좋은 코드 https://www.acmicpc.net/source/30229014

N, H = map(int, input().split())
arr = [0]*H

# 입력을 받을 때 아래쪽 종유석의 높이에는 -를 위쪽 종유석은 +로 표시하여 높이가 올라가게 되어

flag = 1
for _ in range(N):
    _input = int(input())
    if flag == 1:
        arr[_input] -= 1
    else:
        arr[-_input] += 1
    flag *= -1
# 아래 종유석이 사라지면 장애물이 없어지고 위쪽 종유석을 만나면 장애물이 생기는 것을 이용하여 카운팅함
num = N//2  # 그래서 시작되는 값은 아래쪽 종유석의 개수인 N의 절반으로 함
_min = N
cnt = 0
for a in arr:
    num += a
    if num < _min:
        _min = num
        cnt = 1
    elif num == _min:
        cnt += 1

print(_min, cnt)