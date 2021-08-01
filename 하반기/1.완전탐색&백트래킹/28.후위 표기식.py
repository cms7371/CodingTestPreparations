# https://www.acmicpc.net/problem/1918
equation = input()
stack = []
result = ""
op1 = ['+', '-']
op2 = ['*', '/']
for c in equation:
    if c == "(":
        stack.append(c)
    elif c == ")":
        while True:
            last = stack.pop()
            if last != "(":
                result += last
            else:
                break
    elif c.isalpha():
        result += c
    elif c in op1:
        while stack and (stack[-1] in op1 or stack[-1] in op2):
            result += stack.pop()
        stack.append(c)
    elif c in op2:
        while stack and stack[-1] in op2:
            result += stack.pop()
        stack.append(c)
while stack:
    result += stack.pop()
print(result)