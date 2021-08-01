# https://www.acmicpc.net/problem/15732

N, K, D = map(int, input().split())
rule = [tuple(map(int, input().split())) for _ in range(K)]
l, r = 1, N
while l <= r:
    mid = (l + r) // 2
    cur_D = D
    for low, high, inter in rule:
        if mid >= high:
            cur_D -= (high - low) // inter + 1
        elif mid >= low:
            cur_D -= (mid - low) // inter + 1
        if cur_D < 0:
            break
    if cur_D > 0:
        l = mid + 1
    else:
        r = mid - 1
print(l)