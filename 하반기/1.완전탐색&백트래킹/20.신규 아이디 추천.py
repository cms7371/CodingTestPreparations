# https://programmers.co.kr/learn/courses/30/lessons/72410
# 2021 KAKAO BLIND RECUITMENT


def solution(new_id):
    answer = new_id.lower()
    buf = ''
    for c in answer:
        if c.islower() or c.isnumeric() or c in ['-', '_', '.']:
            buf += c
    answer = buf
    if answer:
        i = 0
        while i < len(answer):
            if answer[i] == '.':
                j = i
                while j < len(answer) and answer[j] == '.':
                    j += 1
                answer = answer[:i + 1] + answer[j:]
            i += 1
    if answer and answer[0] == '.': answer = answer[1:]
    if answer and answer[-1] == '.': answer = answer[:-1]
    if not answer: answer = 'a'
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.': answer = answer[:-1]
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("abcdefghijklmn.p"))
print(solution(	"123_.def"))
print(solution(	"=.="))
print(solution("z-+.^."))
print(solution(''))