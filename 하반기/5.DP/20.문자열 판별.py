# https://www.acmicpc.net/problem/16500
# 주어진 단어 중 다른 단어를 포함할 수 있는 경우가 있으므로 맨 뒤에서부터 dp로 확인해야함
s = input()
n = int(input())
words = [input() for _ in range(n)]
dp = [False] * (len(s) + 1)
dp[-1] = True
for pos in range(len(s) - 1, -1, -1):
    for w in words:
        if pos + len(w) <= len(s) and dp[pos + len(w)] and s[pos:pos + len(w)] == w:
            dp[pos] = True
            break
print(int(dp[0]))

# 단순하게 모든 문자열이 매칭될 수 있는지로는 안됨 접근 방식을 달리 해야함
from collections import defaultdict
s = input()
s_dict = defaultdict(int)
n = int(input())
words = [input() for _ in range(n)]
a_dict = defaultdict(int)
for w in words:
    a_dict[w] += 1
idx = 0
while idx < len(s):
    offset = 0
    for w in a_dict:
        if w == s[idx:idx + len(w)]:
            s_dict[w] += 1
            offset = len(w)
            break
    if offset == 0:
        break
    else:
        idx += offset
if idx == len(s) and all([w in s_dict and s_dict[w] >= a_dict[w] for w in a_dict]):
    print(1)
else:
    print(0)