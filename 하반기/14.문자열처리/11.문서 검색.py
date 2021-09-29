# https://www.acmicpc.net/problem/1543
import re
a, b = input(), input()
print(len(re.findall(b, a)))