import re
# 정규식 ((?=() 설명은 https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches-with-a-regexp


def solution(line1, line2):
    space = 0
    answer = 0
    while len(line1) >= len(line2) + (len(line2) - 1) * space:
        crit = '(?=(' + ("." * space).join(list(line2)) + '))'
        result = re.findall(re.compile(crit), line1)
        answer += len(result)
        space += 1
        if len(line2) == 1:
            break
    return answer


print(solution('aaaaa', 'aaaaa'))