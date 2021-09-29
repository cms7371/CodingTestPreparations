# https://www.acmicpc.net/problem/2096
import sys
input = sys.stdin.readline
INF = 10 ** 10
N = int(input())
init = list(map(int, input().split()))
min_arr = init[:]
max_arr = init[:]
for _ in range(N - 1):
    arr = list(map(int, input().split()))
    n_min = [INF] * 3
    n_max = [0] * 3
    for i in range(3):
        for j in range(max(i - 1, 0), min(i + 2, 3)):
            n_min[j] = min(n_min[j], min_arr[i] + arr[j])
            n_max[j] = max(n_max[j], max_arr[i] + arr[j])
    min_arr, max_arr = n_min, n_max
print(max(max_arr), min(min_arr))
