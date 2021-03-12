# 17609번 회문 https://www.acmicpc.net/problem/17609
n = int(input())
cases = []
for _ in range(n):
    cases.append(input())
results = []
for s in cases:
    start, end = 0, len(s) - 1
    isSkipped = False
    notPalindrome = False
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif not isSkipped:
            if start == end - 1:
                isSkipped = True
                break
            elif s[start] == s[end - 1] and s[start + 1] == s[end - 2]:
                end -= 1
                isSkipped = True
            elif s[start + 1] == s[end] and s[start + 2] == s[end - 1]:
                start += 1
                isSkipped = True
            else:
                notPalindrome = True
                break
        else:
            notPalindrome = True
            break
    if notPalindrome:
        results.append(2)
    elif isSkipped:
        results.append(1)
    else:
        results.append(0)
for r in results:
    print(r)
