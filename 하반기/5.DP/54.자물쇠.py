# https://www.acmicpc.net/problem/1514


def dist(a, b):
    if a == b:
        return 0
    if a < b:
        clock_d = b - a
        counter_d = a - b + 10
    else:
        clock_d = b - a + 10
        counter_d = a - b
    if clock_d > counter_d:
        return -counter_d
    else:
        return clock_d


INF = 10 ** 9
N = int(input())
start, end = input(), input()
dp = [[INF] * 10 for _ in range(N)]





