from bisect import bisect_left, bisect_right


n, x = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = bisect_left(numbers, x), bisect_right(numbers, x)
if start == end:
    print(-1)
else:
    print(end - start)

