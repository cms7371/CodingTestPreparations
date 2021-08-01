# https://www.acmicpc.net/problem/1756
def binary_search(arr, val, r):
    l = 0
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= val:
            l = mid + 1
        elif arr[mid] < val:
            r = mid - 1
    return r


d, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))
for i in range(1, d):
    oven[i] = min(oven[i], oven[i - 1])
current_d = len(oven)
for d in doughs:
    current_d = binary_search(oven, d, current_d - 1)
    if current_d == -1:
        break
print(current_d + 1)