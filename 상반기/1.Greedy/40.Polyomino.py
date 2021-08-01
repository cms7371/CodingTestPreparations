# 1343번 폴리오미노 https://www.acmicpc.net/problem/1343
s = input()
result = ""
count = 0
for i in range(len(s)):
    if s[i] == "X":
        count += 1
        if i == len(s) - 1:
            if count >= 2 and count % 2 == 0:
                result += "AAAA" * (count // 4) + "BB" * ((count % 4) // 2)
            else:
                result = -1
    else:
        if count != 0:
            if count % 2 == 0:
                result += "AAAA" * (count // 4) + "BB" * ((count % 4) // 2)
                count = 0
            else:
                result = -1
                break
        result += "."
print(result)


