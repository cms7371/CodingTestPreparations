# https://www.acmicpc.net/problem/1405
def DFS(y, x, prob, k, stack=None):
    if stack is None:
        stack = {(y, x)}
    for i in range(4):
        dy, dx = offset[i]
        ny, nx = y + dy, x + dx
        if (ny, nx) in stack:
            global result
            result -= prob * p_arr[i]
        elif k < K - 1:
            stack.add((ny, nx))
            DFS(ny, nx, prob * p_arr[i], k + 1, stack)
    stack.remove((y, x))


K, p1, p2, p3, p4 = map(int, input().split())
p_arr = [p1 / 100, p2 / 100, p3 / 100, p4 / 100]
offset = [(0, 1), (0, -1), (-1, 0), (1, 0)]
result = 1
DFS(0, 0, 1, 0)
print(result)