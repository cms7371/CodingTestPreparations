from itertools import combinations


def solution(places):
    answer = []
    for place in places:
        positions = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    positions.append((i, j))
        comb_positions = combinations(positions, 2)
        is_proper = True
        for p1, p2 in comb_positions:
            dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            if dist == 2:
                if p1[0] == p2[0]:
                    if place[p1[0]][(p1[1] + p2[1]) // 2] != "X":
                        is_proper = False
                        break
                elif p1[1] == p2[1]:
                    if place[(p1[0] + p2[0]) // 2][p1[1]] != "X":
                        is_proper = False
                        break
                else:
                    if place[p1[0]][p2[1]] != "X" or place[p2[0]][p1[1]] != "X":
                        is_proper = False
                        break
            if dist == 1:
                is_proper = False
                break
        answer.append(int(is_proper))
    return answer
