# 1201번 NMK https://www.acmicpc.net/problem/1201
n, m, k = map(int, input().split())
if m == 1 and k == n:
    print(" ".join(map(str, range(n, 0, -1))))
elif m == n and k == 1:
    print(" ".join(map(str, range(1, n + 1))))
elif m * k >= n and m + k <= n + 1:
    result = [i for i in range(1, n + 1)]
    result[:k] = result[:k][::-1]
    m -= 1
    togo = (n - k)
    i = k
    while m > 0:
        if togo % m == 0:
            interval = togo // m
        else:
            interval = togo // m + 1
        result[i:i + interval] = result[i:i+interval][::-1]
        i += interval
        togo -= interval
        m -= 1
    print(" ".join(map(str, result)))
else:
    print(-1)


