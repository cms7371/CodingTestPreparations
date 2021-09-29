# https://www.acmicpc.net/problem/4256
def post(i, l, r, p_arr, i_arr):
    cur = p_arr[i]
    mid = i_arr.index(cur, l)
    if mid - 1 >= l:
        post(i + 1, l, mid - 1, p_arr, i_arr)
    if mid + 1 <= r:
        post(i + mid - l + 1, mid + 1, r, p_arr, i_arr)
    print(cur, end=' ')


T = int(input())
for _ in range(T):
    N = int(input())
    p_tree = list(map(int, input().split()))
    i_tree = list(map(int, input().split()))
    post(0, 0, N - 1, p_tree, i_tree)
    print("")
