# https://www.acmicpc.net/problem/5076
import re
while True:
    s = input()
    if s == "#":
        break
    tags = re.findall('<.*?>', s)
    stack = []
    for tag in tags:
        if tag.startswith('</'):
            if tag.endswith('/>'):
                stack.append(False)
                break
            else:
                if stack and stack[-1] == tag[2:-1].split()[0]:
                    stack.pop()
                else:
                    stack.append(False)
                    break
        else:
            if tag.endswith('/>'):
                continue
            else:
                stack.append(tag[1:-1].split()[0])
    print('legal' if not stack else 'illegal')