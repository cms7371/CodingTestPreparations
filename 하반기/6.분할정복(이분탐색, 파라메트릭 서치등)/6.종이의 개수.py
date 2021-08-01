# https://www.acmicpc.net/problem/1780
import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


def solve(y, x, r, out=None):
    if out is None:
        out = [0] * 3
    temp = paper[y][x]
    for i in range(y, y + r):
        for j in range(x, x + r):
            if paper[i][j] != temp:
                rr = r // 3
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        solve(y + rr * ii, x + rr * jj, rr, out)
                return out
    out[temp + 1] += 1
    return out


print(*solve(0, 0, N), sep='\n')