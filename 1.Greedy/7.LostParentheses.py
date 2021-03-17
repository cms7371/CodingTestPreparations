# 1541번 잃어버린 괄호 https://www.acmicpc.net/problem/1541
# 2회차
s = input()
isPlus = True
buffer = ""
result = 0
for c in s:
    if c.isnumeric():
        buffer += c
    else:
        result = result + int(buffer) if isPlus else result - int(buffer)
        buffer = ""
        if isPlus and c == "-":
            isPlus = False
result = result + int(buffer) if isPlus else result - int(buffer)
print(result)

# 1회차
s = input()
buffer = ""
data = []
for c in s:
    if c.isnumeric():
        buffer += c
    else:
        data.append(buffer)
        buffer = ""
        data.append(c)
data.append(buffer)
isPlus = True
result = 0
for d in data:
    if d.isnumeric():
        if isPlus:
            result += int(d)
        else:
            result -= int(d)
    else:
        if d == "-":
            isPlus = False
print(result)

