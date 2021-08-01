# https://www.acmicpc.net/problem/1074
def solve(n, r, c):
    if n == 0:
        return 1
    half = 2 ** (n - 1)
    o = 2 ** ((n - 1) * 2)
    return o * (c // half) + 2 * o * (r // half) + solve(n - 1, r % half, c % half)


print(solve(*map(int, input().split())) - 1)