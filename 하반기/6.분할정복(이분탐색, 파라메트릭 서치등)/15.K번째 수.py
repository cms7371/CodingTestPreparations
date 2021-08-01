# https://www.acmicpc.net/problem/1300
N = int(input())
K = int(input())
l, r = 1, N * N
while l <= r:
    mid = (l + r) // 2
    lows = 0
    for i in range(1, min(mid, N) + 1):
        lows += min(N, (mid - 1) // i)  # mid보다 작은 수를 센다
    if lows < K:
        l = mid + 1
    else:
        r = mid - 1
print(r)
