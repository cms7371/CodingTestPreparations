# UCPC https://www.acmicpc.net/problem/15904
s = input()
ucpc = ["U", "C", "P", "C"]
i = 0
j = 0
while i < 4 and j < len(s):
    if s[j] == ucpc[i]:
        i += 1
    j += 1
print("{0}".format("I love UCPC" if i == 4 else "I hate UCPC"))



