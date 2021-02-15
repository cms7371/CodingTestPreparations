# 문제 : 곱하기 또는 더하기
# 0~9 로 이루어진 문자열 s가 주어졌을 때 문자열의 각 자리를 모두 확인하여 사이에 + 또는 *를 넣어 계산하여 얻어질 수 있는 최댓값을 구하여라
# 단 일반적인 연산과는 다르게 모든 연산은 왼쪽부터 순서대로 이루어진다.

# 내 코드
s = input()
result = 0
for c in s:
    if result == 0:
        result += int(c)
    else:
        n = int(c)
        if n > 1:
            result *= n
        else:
            result += n
print(result)
# 예시 코드
data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)