# https://programmers.co.kr/learn/courses/30/lessons/81301
# 2021 카카오 채용연계형 인턴십


def solution(s):
    alpha_to_num = [("zero", '0'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'),
                    ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]
    answer = s
    for alpha, num in alpha_to_num:
        answer = answer.replace(alpha, num)
    answer = int(answer)
    return answer


print(solution("one4seveneight"))