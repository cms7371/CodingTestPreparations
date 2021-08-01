# https://www.acmicpc.net/problem/2304
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()
stack = [arr[0]]
result = 0
for i in range(1, N):
    if arr[i][1] >= stack[-1][1]:
        result += (arr[i][0] - stack[-1][0]) * stack[-1][1]
        stack.append(arr[i])
stack2 = [arr[-1]]
for i in range(N - 1, -1, -1):

    if arr[i][1] >= stack2[-1][1]:
        result += (stack2[-1][0] - arr[i][0]) * stack2[-1][1]
        stack2.append(arr[i])
    if arr[i][0] == stack[-1][0]:
        break
result += stack[-1][1]
print(result)
