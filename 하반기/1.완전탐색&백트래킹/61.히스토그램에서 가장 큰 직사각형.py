# https://www.acmicpc.net/problem/6549
while True:
    input_arr = list(map(int, input().split()))
    if len(input_arr) == 1:
        break
    N = input_arr[0]
    arr = input_arr[1:]
    idx = 0
    stack = []
    result = 0
    while idx < N or stack:
        if not stack or (idx < N and arr[idx] > arr[stack[-1]]):
            stack.append(idx)
            idx += 1
        else:
            left = stack[-2] if len(stack) >= 2 else -1
            result = max(result, arr[stack[-1]] * (idx - left - 1))
            stack.pop()
    print(result)

