# 5373번 큐빙 https://www.acmicpc.net/problem/5373
# 그지같네 진짜... 컨디션 좋을 때 다시 풀기
def rotate(p, counter=False):  # 시계 방향이면 False, 반시계면 True
    if counter:
        p[0][0], p[0][1], p[0][2], p[1][2], p[2][2], p[2][1], p[2][0], p[1][0] = p[0][2], p[1][2], p[2][2], p[2][1], p[2][0], p[1][0], p[0][0], p[0][1]
    else:
        p[0][0], p[0][1], p[0][2], p[1][2], p[2][2], p[2][1], p[2][0], p[1][0] = p[2][0], p[1][0], p[0][0], p[0][1], p[0][2], p[1][2], p[2][2], p[2][1]


U, D, F, B, L, R = range(6)
test_cases = []
for _ in range(int(input())):
    input()
    test_cases.append(input().split())
for commands in test_cases:
    c = [[[color] * 3 for _ in range(3)] for color in "wyrogb"]
    for cmd in commands:
        if cmd == "U+":
            rotate(c[U])
            c[F][0], c[R][0], c[B][0], c[L][0] = c[R][0], c[B][0], c[L][0], c[F][0]
        elif cmd == "U-":
            rotate(c[U], True)
            c[F][0], c[R][0], c[B][0], c[L][0] = c[L][0], c[F][0], c[R][0], c[B][0]
        elif cmd == "D+":
            rotate(c[D])
            c[F][2], c[R][2], c[B][2], c[L][2] = c[L][2], c[F][2], c[R][2], c[B][2]
        elif cmd == "D-":
            rotate(c[D], True)
            c[F][2], c[R][2], c[B][2], c[L][2] = c[R][2], c[B][2], c[L][2], c[F][2]
        elif cmd == "F+":
            rotate(c[F])
            for i in range(3):
                c[U][2][i], c[R][i][0], c[D][2][i], c[L][2 - i][2] = c[L][2 - i][2], c[U][2][i], c[R][i][0], c[D][2][i]
        elif cmd == "F-":
            rotate(c[F], True)
            for i in range(3):
                c[U][2][i], c[R][i][0], c[D][2][i], c[L][2 - i][2] = c[R][i][0], c[D][2][i], c[L][2 - i][2], c[U][2][i]
        elif cmd == "B+":
            rotate(c[B])
            for i in range(3):
                c[U][0][i], c[R][i][2], c[D][0][i], c[L][2 - i][0] = c[R][i][2], c[D][0][i], c[L][2 - i][0], c[U][0][i]
        elif cmd == "B-":
            rotate(c[B], True)
            for i in range(3):
                c[U][0][i], c[R][i][2], c[D][0][i], c[L][2 - i][0] = c[L][2 - i][0], c[U][0][i], c[R][i][2], c[D][0][i]
        elif cmd == "R+":
            rotate(c[R])
            for i in range(3):
                c[U][i][2], c[F][i][2], c[D][2 - i][0], c[B][2 - i][0] = c[F][i][2], c[D][2 - i][0], c[B][2 - i][0], c[U][i][2]
        elif cmd == "R-":
            rotate(c[R], True)
            for i in range(3):
                c[U][i][2], c[F][i][2], c[D][2 - i][0], c[B][2 - i][0] = c[B][2 - i][0], c[U][i][2], c[F][i][2], c[D][2 - i][0]
        elif cmd == "L+":
            rotate(c[L])
            for i in range(3):
                c[U][i][0], c[F][i][0], c[D][2 - i][2], c[B][2 - i][2] = c[B][2 - i][2], c[U][i][0], c[F][i][0], c[D][2 - i][2]
        elif cmd == "L-":
            rotate(c[L], False)
            for i in range(3):
                c[U][i][0], c[F][i][0], c[D][2 - i][2], c[B][2 - i][2] = c[F][i][0], c[D][2 - i][2], c[B][2 - i][2], c[U][i][0]
    for i in range(3):
        print("".join(c[U][i]))



