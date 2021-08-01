# 문제 : 병사 배치하기
# n명의 병사가 있고 각각 병사마다 전투력이 있다. 이때 주어진 병사 중 일부를 열외했을 때 병사의 전투력이 내림차순으로 배치 될 수 있도록
# 하는 열외 병사의 최소 수를 구하여라

# 내 풀이
# 주어진 병사들을 내려가는 그룹으로 쪼개고 이 그룹들을 비교해서 적절하게 판단하여 붙여 결과값을 얻는다 -> 실패
n = int(input())
array = list(map(int, input().split()))

partitions = []
temp = 0
for i in range(1, n):
    if array[i - 1] <= array[i]:
        partitions.append(array[temp:i])
        temp = i
    if i == n - 1:
        partitions.append(array[temp:i+1])
result = partitions[0]
for i in range(1, len(partitions)):
    if partitions[i][0] < result[-1]:
        result = result + partitions[i]
    else:
        rear_max = partitions[i][0]
        j = 1
        current_len = len(result)
        while j < current_len and result[-j-1] <= rear_max:
            j += 1
        if j < len(partitions[i]):
            result = result[:-j] + partitions[i]
        elif j == len(partitions[i]) and result[-1] < partitions[i][-1]:
            result = result[:-j] + partitions[i]
print(n - len(result))

n = int(input())
array = list(map(int, input().split()))
array.reverse()
d = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))
