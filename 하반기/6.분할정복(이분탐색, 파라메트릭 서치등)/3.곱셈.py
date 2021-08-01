# https://www.acmicpc.net/problem/1629

A, B, C = map(int, input().split())
stack = []
while B != 1:
    if B % 2 == 0:
        stack.append(True)
        B //= 2
    else:
        stack.append(False)
        B -= 1
result = A % C
while stack:
    if stack.pop():
        result = (result * result) % C
    else:
        result = (result * A) % C
print(result)