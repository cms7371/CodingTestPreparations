# https://www.acmicpc.net/problem/16434
import sys
input = sys.stdin.readline
N, A = map(int, input().split())
dungeon = [tuple(map(int, input().split())) for _ in range(N)]
l, r = 0, 10 ** 20
while l <= r:
    H_max = (l + r) // 2
    H_cur = H_max
    A_cur = A
    for i in range(N):
        room = dungeon[i]
        if room[0] == 1:
            _, M_a, M_h = room
            attack_turn = (M_h + A_cur - 1) // A_cur
            H_cur -= (attack_turn - 1) * M_a
            if H_cur <= 0:
                break
        else:
            H_cur = min(H_max, H_cur + room[2])
            A_cur += room[1]
    if i == N - 1 and H_cur > 0:
        r = H_max - 1
    else:
        l = H_max + 1
print(l)
