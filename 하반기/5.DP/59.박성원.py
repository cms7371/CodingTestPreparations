# https://www.acmicpc.net/problem/1086
from math import factorial


def gcd(a, b):
    MOD = a % b
    if MOD:
        return gcd(b, MOD)
    else:
        return b


N = int(input())
arr = [input() for _ in range(N)]
K = int(input())
arr_mod = []
arr_l = []
ten_mod = [0] * 51
ten_mod[0] = 1 % K
for t in range(1, 51):
    ten_mod[t] = (ten_mod[t - 1] * 10) % K
for i in range(N):
    arr_l.append(len(arr[i]))
    arr_mod.append(0)
    for j in range(arr_l[i]):
        arr_mod[-1] += int(arr[i][j]) * ten_mod[arr_l[i] - j - 1]
    arr_mod[-1] %= K
# dp[m][k] = p 는 mask가 m이고 나머지가 k인 조합의 개수 p
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1
for m in range((1 << N) - 1):
    for k in range(K):
        if dp[m][k]:
            for i in range(N):
                bit = 1 << i
                if not(m & bit):
                    nm = m | bit
                    nk = (k * ten_mod[arr_l[i]] + arr_mod[i]) % K
                    dp[nm][nk] += dp[m][k]
upper = dp[-1][0]
lower = factorial(N)
if upper:
    div = gcd(lower, upper)
    print(f"{upper // div}/{lower // div}")
else:
    print('0/1')
