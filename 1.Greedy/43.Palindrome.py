# 17609번 회문 https://www.acmicpc.net/problem/17609
# 복습 풀이
t = int(input())
words = [input() for _ in range(t)]
output = []
for w in words:
    s, e = 0, len(w) - 1
    result = 0
    while s <= e:
        if w[s] == w[e]:
            s += 1
            e -= 1
        elif result == 1:
            result = 2
            break
        else:
            if e - s < 2:
                result = 1
                break
            elif w[s] == w[e - 1] and w[s + 1] == w[e - 2]:
                e -= 1
                result = 1
            elif w[e] == w[s + 1] and w[e - 1] == w[s + 2]:
                s += 1
                result = 1
            else:
                result = 2
                break
    output.append(str(result))
print("\n".join(output))

# 내 풀이
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
