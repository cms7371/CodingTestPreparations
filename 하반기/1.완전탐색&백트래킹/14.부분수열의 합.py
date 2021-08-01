# https://www.acmicpc.net/problem/1182
# 비트마스크와 브루트 포스를 같이 이용
n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
for mask in range(1, pow(2, n)):
    mask = ("{:0>" + str(n) + "b}").format(mask)
    current = 0
    for i in range(n):
        if mask[i] == '1':
            current += nums[i]
    if current == s:
        result += 1
print(result)


"231".split()