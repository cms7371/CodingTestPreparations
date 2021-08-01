# https://www.acmicpc.net/problem/1725
# 이번엔 스택을 이용한 풀이
import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
stack = []
result = 0
for i in range(N + 1):
    while stack and (i == N or arr[stack[-1]] >= arr[i]):
        cur_min = arr[stack.pop()]
        left, right = stack[-1] if stack else -1, i - 1
        result = max(result, cur_min * (right - left))
    stack.append(i)
print(result)