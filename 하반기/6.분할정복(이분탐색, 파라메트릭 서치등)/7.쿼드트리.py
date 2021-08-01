# https://www.acmicpc.net/problem/1992
import sys
N = int(sys.stdin.readline())
arr = [list(map(int, list(sys.stdin.readline())[:-1])) for _ in range(N)]


def solve(y, x, r):
    temp = arr[y][x]
    for i in range(y, y + r):
        for j in range(x, x + r):
            if arr[i][j] != temp:
                rr = r // 2
                result = '('
                for ry in range(2):
                    for rx in range(2):
                        result += solve(y + rr * ry, x + rr * rx, rr)
                return result + ')'
    return str(temp)


print(solve(0, 0, N))