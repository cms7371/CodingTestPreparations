def solution(n, k, cmd):
    table = [i for i in range(n)]
    del_list = []
    for c in cmd:
        if c[0] == "U":
            offset = int(c.split()[1])
            k -= offset
        elif c[0] == "D":
            offset = int(c.split()[1])
            k += offset
        elif c[0] == "C":
            del_list.append((table[k], k))  # 값, 위치로 저장
            del table[k]
            if k >= len(table):
                k = len(table) - 1
        elif c[0] == "Z":
            val, position = del_list.pop()
            table.insert(position, val)
            if position <= k:
                k += 1
    answer = ''
    idx = 0
    for i in range(n):
        if idx < len(table) and i == table[idx]:
            answer += "O"
            idx += 1
        else:
            answer += "X"
    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
