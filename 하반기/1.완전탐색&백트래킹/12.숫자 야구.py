# https://www.acmicpc.net/problem/2503
def cal(subject, target):
    strike, ball = 0, 0
    for i in range(3):
        if subject[i] == target[i]:
            strike += 1
        elif subject[i] in target:
            ball += 1
    return strike, ball


n = int(input())
crits = []
for _ in range(n):
    num, s, b = map(int, input().split())
    num = str(num)
    crits.append((num, s, b))
result = 0
for now in range(100, 1000):
    now = str(now)
    if now.count(now[0]) > 1 or now.count(now[1]) > 1 or '0' in now:
        continue
    is_ok = True
    for num, s_ans, b_ans in crits:
        s_now, b_now = cal(now, num)
        if s_now == s_ans and b_now == b_ans:
            continue
        else:
            is_ok = False
            break
    if is_ok:
        result += 1
print(result)