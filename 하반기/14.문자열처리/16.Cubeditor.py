# https://www.acmicpc.net/problem/1701


def get_pi(search):
    pi = [0] * len(search)
    idx, matched = 1, 0
    while idx + matched < len(search):
        if search[matched] == search[idx + matched]:
            matched += 1
            pi[idx + matched - 1] = matched
        else:
            if matched == 0:
                idx += 1
            else:
                idx += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


s = input()
result = 0
for i in range(len(s) - 1):
    result = max(result, max(get_pi(s[i:])))
print(result)