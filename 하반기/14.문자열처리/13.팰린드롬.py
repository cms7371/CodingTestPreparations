# https://www.acmicpc.net/problem/2079


def is_palindrome(string):
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


s = input()
dp = [10 ** 9] * (len(s) + 1)
dp[0], dp[1] = -1, 0
for i in range(1, len(s)):
    for j in range(i + 1):
        if is_palindrome(s[j:i + 1]):
            dp[i + 1] = min(dp[i + 1], dp[j] + 1)
print(dp[-1] + 1)