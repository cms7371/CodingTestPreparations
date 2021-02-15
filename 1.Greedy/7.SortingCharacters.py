# 문제 : 문자열 재정렬
# 숫자와 알파벳으로 구성된 문자열이 주어졌을 때 알파벳은 순서대로 정렬하고, 숫자는 모두 더해서 알파벳+숫자 순서로 출력하라

data = input()
number = 0
chars = []
for c in data:
    try:
        number += int(c)
    except:
        chars.append(c)
chars.sort()
print("".join(chars) + str(number))

# 예시 코드
data = input()
result = []
value = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))
print("".join(result))
