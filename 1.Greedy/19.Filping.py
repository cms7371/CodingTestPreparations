# 1439번 뒤집기 https://www.acmicpc.net/problem/1439
s = input()
if s[0] == '0':
    isOne = False
else:
    isOne = True
oneCount = 0
zeroCount = 0
for i in range(1, len(s)):
    if s[i] == "0":
        if isOne:
            oneCount += 1
            isOne = False
    else:
        if not isOne:
            zeroCount += 1
            isOne = True
if s[-1] == '0':
    zeroCount += 1
else:
    oneCount += 1
print(min(zeroCount, oneCount))


