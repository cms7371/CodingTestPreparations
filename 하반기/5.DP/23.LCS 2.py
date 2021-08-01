# https://www.acmicpc.net/problem/9252
str1 = input()
str2 = input()
dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
for pos2 in range(1, len(str2) + 1):
    for pos1 in range(1, len(str1) + 1):
        if str2[pos2 - 1] == str1[pos1 - 1]:
            dp[pos2][pos1] = dp[pos2 - 1][pos1 - 1] + 1
        else:
            dp[pos2][pos1] = max(dp[pos2][pos1 - 1], dp[pos2 - 1][pos1])
result = ''
pos1, pos2 = len(str1), len(str2)
while dp[pos2][pos1]:
    if dp[pos2][pos1] == dp[pos2][pos1 - 1]:
        pos1 -= 1
    elif dp[pos2][pos1] == dp[pos2 - 1][pos1]:
        pos2 -= 1
    else:
        pos1 -= 1
        pos2 -= 1
        result += str2[pos2]
print(dp[-1][-1], result[::-1], sep='\n')