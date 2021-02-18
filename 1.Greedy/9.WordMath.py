# 1339번 단어 수학 https://www.acmicpc.net/problem/1339
# 그리디 구현 2 : 각 자리에 해당하는 가중치 부여(1의 자리면 1 10자리면 10)
n = int(input())
words = [input() for _ in range(n)]
dic = dict()
for word in words:
    for i in range(len(word)):
        weight = pow(10, len(word) - i - 1)
        c = word[i]
        if c in dic:
            dic[c] += weight
        else:
            dic[c] = weight
dic = [(c, dic[c]) for c in dic]
dic.sort(key=lambda a: a[1], reverse=True)
alpha_to_num = dict()
for i in range(len(dic)):
    alpha_to_num[dic[i][0]] = str(9 - i)
result = 0
buffer = ""
for word in words:
    for c in word:
        buffer += alpha_to_num[c]
    result += int(buffer)
    buffer = ""
print(result)

# 그리디 구현 1 : 각 자리수를 모두 체크하여 높은 자리를 가진 알파벳에 더 높은 우선순위를 부여한다
# 실패(반례 존재) -> ABB BB BB --로 낮은 자리가 10개 이상 되면 더 높은 우선순위를 갖게 됨
n = int(input())
words = [input() for _ in range(n)]
dic = dict()
for word in words:
    for i in range(len(word)):
        position = len(word) - i
        c = word[i]
        if c in dic:
            dic[c].add(position)
        else:
            dic[c] = {position}
for c in dic:
    dic[c] = list(dic[c])
    dic[c].sort(reverse=True)
priority_list = [dic[c] + [c] for c in dic]
priority_list.sort(key=lambda a: a[:-1], reverse=True)
alpha_to_num = dict()
for i in range(len(priority_list)):
    alpha_to_num[priority_list[i][-1]] = str(9 - i)
result = 0
buffer = ""
for word in words:
    for c in word:
        buffer += alpha_to_num[c]
    result += int(buffer)
    buffer = ""
print(result)

# 브루트포스
from itertools import permutations

n = int(input())
words = [input() for _ in range(n)]
alphas = set()
for word in words:
    alphas = alphas.union(set(word))
num_sets = list(permutations(range(9, 9 - len(alphas), -1)))
alphas = list(alphas)
result = []
for nums in num_sets:
    dic = dict()
    for i in range(len(alphas)):
        dic[alphas[i]] = str(nums[i])
    local_sum = 0
    for word in words:
        num = ""
        for c in word:
            num += dic[c]
        local_sum += int(num)
    result.append(local_sum)
print(max(result))
# 알파벳이 많아지니 매우 느림...
