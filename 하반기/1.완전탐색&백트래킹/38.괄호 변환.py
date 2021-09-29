
def correct_string(w):
    if is_balanced(w):
        return w
    # w를 u와 v로 분리
    weight = 1 if w[0] == '(' else -1
    i = 1
    while i < len(w) and weight:
        weight += 1 if w[i] == '(' else -1
        i += 1
    u, v = w[:i], w[i:]
    cv = correct_string(v)
    if is_balanced(u):
        return u + cv
    ru = "".join(map(lambda c: ")" if c == "(" else "(", u[1:-1]))
    return "(" + cv + ")" + ru


def is_balanced(s):
    weight = 0
    for c in s:
        if c == '(':
            weight += 1
        else:
            weight -= 1
        if weight < 0:
            return False
    return True



def solution(p):
    return correct_string(p)