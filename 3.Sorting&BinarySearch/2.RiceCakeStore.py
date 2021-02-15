import bisect


n, m = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort()
min_h = cakes[0]
max_h = cakes[-1]
while True:
    mid_h = (min_h + max_h) // 2
    mid_index = bisect.bisect_right(cakes, mid_h)
    sliced_cakes_h = sum(cakes[mid_index:]) - (len(cakes) - mid_index) * mid_h
    if sliced_cakes_h > m:
        min_h = mid_h + 1
    elif sliced_cakes_h < m:
        max_h = mid_h - 1
    elif sliced_cakes_h == m:
        break
print(mid_h)

