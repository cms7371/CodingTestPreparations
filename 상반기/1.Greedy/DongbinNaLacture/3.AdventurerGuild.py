# 문제 : 모험가 길드
# 한 마을에 N명의 모험가가 있어 이들에게 공포도를 측정합니다. 이때 공포도가 X인 모험가는 반드시 X명 이상의 인원을 가진 그룹에 참여해야합니다.
# N명에 대한 모험가의 정보가 주어졌을 때 여행을 떠날 수 있는 그룹의 최댓값을 구하는 프로그램을 작성하세요.
# 모험가는 마을에 남아도 되기 때문에 꼭 다 넣을 필요는 없습니다.

# 내 풀이
# 공포도가 1 -> 혼자 가도 됨, 공포도가 2 -> 2인 사람 둘이 가는게 최적 이런 방식으로 그룹을 자른다
# 이때 연산 횟수를 낮추기 위해 모든 모험가를 조회하는 것이 아닌 그룹의 가장 끝의 모험가의 공포도를 조회해서
# 그룹을 재정의함
n = int(input())
fear_list = list(map(int, input().split()))
fear_list.sort()
result_group = list()
max_index = len(fear_list)
start = 0
end = 0
result = 0
while start < max_index:
    target = fear_list[start]
    end = start + target
    try:
        while fear_list[end - 1] > end - start:
            end = start + fear_list[end - 1]
    except IndexError:
        break
    result += 1
    start = end
print(result)

# 예시 코드(단순 조회로 해결)
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 그룹의 수
count = 0  # 현재 그룹의 모험가 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
