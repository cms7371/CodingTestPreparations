# https://www.acmicpc.net/problem/1019


def solve(s, e, exp, result):
    temp = [0] * 10
    while str(s)[-1] != '0' and s <= e:
        for c in str(s):
            temp[int(c)] += 1
        s += 1
    while str(e)[-1] != '9' and e >= s:
        for c in str(e):
            temp[int(c)] += 1
        e -= 1
    if e > s:
        ns, ne = s // 10, e // 10
        count = ne - ns + 1
        for d in range(10):
            temp[d] += count
        solve(ns, ne, exp + 1, result)
    for d in range(10):
        result[d] += temp[d] * (10 ** exp)


N = int(input())
answer = [0] * 10
solve(1, N, 0, answer)
print(*answer)