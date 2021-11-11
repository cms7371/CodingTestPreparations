# https://www.acmicpc.net/problem/7682

while True:
    case = input()
    if case == "end":
        break
    x_count = case.count('X')
    o_count = case.count('O')
    if not (x_count == o_count or x_count == o_count + 1):
        print("invalid")
        continue
    x_line_count, o_line_count = 0, 0
    for i in range(0, 9, 3):
        if case[i:i + 3].count('X') == 3:
            x_line_count += 1
        elif case[i: i + 3].count('O') == 3:
            o_line_count += 1
    for i in range(3):
        if case[i:9:3].count('X') == 3:
            x_line_count += 1
        elif case[i:9:3].count('O') == 3:
            o_line_count += 1
    if case[0:9:4].count('X') == 3:
        x_line_count += 1
    if case[0:9:4].count('O') == 3:
        o_line_count += 1
    if case[2:7:2].count('X') == 3:
        x_line_count += 1
    if case[2:7:2].count('O') == 3:
        o_line_count += 1
    if (x_line_count and not o_line_count and x_count > o_count) or (
            o_line_count and not x_line_count and x_count == o_count) or (
            not x_line_count and not o_line_count and x_count + o_count == 9):
        print("valid")
    else:
        print("invalid")
