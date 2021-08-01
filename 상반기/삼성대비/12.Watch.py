# 15683번 감시 https://www.acmicpc.net/problem/15683
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]
cctv_position = []
cctv_masks = []
result = 0
for i in range(n):
    for j in range(m):
        if 0 < origin[i][j] < 6:
            num = origin[i][j]
            cctv_position.append((i, j))
            masks = []
            if num == 1:
                for d in range(4):
                    mask = [False] * 4
                    mask[d] = True
                    masks.append(tuple(mask))
            elif num == 2:
                masks.append((True, False, True, False))
                masks.append((False, True, False, True))
            elif num == 3:
                for d in range(4):
                    mask = [False] * 4
                    mask[d], mask[(d + 1) % 4] = True, True
                    masks.append(tuple(mask))
            elif num == 4:
                for d in range(4):
                    mask = [False] * 4
                    mask[(d - 1) % 4], mask[d], mask[(d + 1) % 4] = True, True, True
                    masks.append(tuple(mask))
            else:
                masks.append((True, True, True, True))
            cctv_masks.append(masks)
        elif origin[i][j] == 0:
            result += 1
bit_len = len(cctv_position)
bit_mask = [0] * bit_len
bit_mask_limit = [len(cctv_masks[i]) for i in range(bit_len)]
while cctv_position:
    # 맵을 복사
    current_map = [origin[i][:] for i in range(n)]
    # bit_mask를 이용하여 마스크를 탐험해주고 맵을 갱신
    for i in range(bit_len):
        x, y = cctv_position[i]
        current_mask = cctv_masks[i][bit_mask[i]]
        for direction in range(4):
            if current_mask[direction]:
                o = offsets[direction]
                nx, ny = x + o[0], y + o[1]
                while 0 <= nx < n and 0 <= ny < m and current_map[nx][ny] != 6:
                    if current_map[nx][ny] == 0:
                        current_map[nx][ny] = -1
                    nx, ny = nx + o[0], ny + o[1]
    current_result = sum([current_map[i].count(0) for i in range(n)])
    result = min(result, current_result)
    # bit_mask 증가함. 이때 맨 처음 것이 limit와 같아지면 모두 돌았다는 뜻이므로 스탑
    bit_mask[-1] += 1
    for i in range(bit_len - 1, 0, -1):  # 오버 플로우 나면 이항
        if bit_mask[i] == bit_mask_limit[i]:
            bit_mask[i] = 0
            bit_mask[i - 1] += 1
    if bit_mask[0] == bit_mask_limit[0]:
        break
print(result)




