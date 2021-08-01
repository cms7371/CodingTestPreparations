# 2212번 센서 https://www.acmicpc.net/problem/2212
# 복습 풀이
n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
interval = [sensor[i] - sensor[i - 1] for i in range(1, n)]
interval.sort()
for _ in range(k - 1):
    interval.pop()
print(sum(interval))
# 센터가 N개라는 것은 각 간격에서 N-1개만큼의 간격을 없앨 수 있다는 이야기가 됨
# 예를 들자면 [1, 3, 5, 7, 9]가 있을 때 간격이 [2, 2, 2, 2]가 되는데 여기서 센서가 1개라면 모든 구간이 결과가 되고
# 2개라면 한 구간의 인터벌을 두고 합을 할 수 있기 때문에 6이 결과되고 3개면 2구간을 제외하고.... 하는 방식으로 할 수 있음
# 결과적으로 N-1개만큼 가장 큰 구간을 제외해버리는 방식으로 구할 수 있음
n = int(input())
k = int(input())
if n <= k:
    print(0)
else:
    positions = list(map(int, input().split()))
    positions.sort()
    intervals = []
    buffer = positions[0]
    for i in range(1, len(positions)):
        if positions[i] != buffer:
            intervals.append(positions[i] - buffer)
        buffer = positions[i]
    intervals.sort()
    print(sum(intervals[:len(intervals) - (k - 1)]))

