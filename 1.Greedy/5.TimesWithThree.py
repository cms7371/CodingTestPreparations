# 문제 : 3이 들어가는 시간 세기
# 23 이하의 양수 N이 주어졌을 때 N시 59분 59초까지 3이 포함된 모든 시각을 카운트하는 프로그램을 작성하라
# 모든 경우의 수를 볼 수 있기 때문에 완전 탐색(Brute Forcing) 문제라고 불림
n = int(input())
h, m, s = 0, 0, 0
count = 0
while h <= n:
    string = "{0:02d}:{1:02d}:{2:02d}".format(h, m, s)

    if "3" in string:
        print(string)
        count += 1
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
print(count)

# 예시 코드
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)