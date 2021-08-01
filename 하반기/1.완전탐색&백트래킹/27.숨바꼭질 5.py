# https://www.acmicpc.net/problem/17071
N, K = map(int, input().split())
visited = [0] * 500001
visited[N] = 1
cur_pos = [N]
time = 0
while K <= 500000:
    # bit masking으로 홀수 시간 짝수 시간 방문 표현
    # 2의 나머지에서 1을 더해 짝수에는 1에 홀수에는 2에 마스킹
    if visited[K] and ((time % 2) + 1) & visited[K]:
        break
    time += 1
    next_pos = []
    mask = (time % 2) + 1
    for pos in cur_pos:
        if pos > 0 and not visited[pos - 1] & mask:
            visited[pos - 1] |= mask
            next_pos.append(pos - 1)
        if pos < 500000 and not visited[pos + 1] & mask:
            visited[pos + 1] |= mask
            next_pos.append(pos + 1)
        if pos * 2 <= 500000 and not visited[pos * 2] & mask:
            visited[pos * 2] |= mask
            next_pos.append(pos * 2)
    cur_pos = next_pos
    K += time
print(time if K <= 500000 else -1)

cur_pos = set()
cur_pos.add(N)
time = 0
while K <= 500000:
    if K in cur_pos:
        break
    next_pos = set()
    for pos in cur_pos:
        if pos > 0:
            next_pos.add(pos - 1)
        if pos < 500000:
            next_pos.add(pos + 1)
        if pos * 2 <= 500000:
            next_pos.add(pos * 2)
    cur_pos = next_pos
    time += 1
    K += time
print(time if K <= 500000 else -1)