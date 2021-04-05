# 5639번 이진 검색 트리 https://www.acmicpc.net/problem/5639
import sys
def put(node, num):
    if node == num:
        tree[node] = [None, None]
    elif node < num:
        if tree[node][1] is None:
            tree[node][1] = num
        put(tree[node][1], num)
    elif node > num:
        if tree[node][0] is None:
            tree[node][0] = num
        put(tree[node][0], num)
def explore(node):
    if tree[node]:
        if tree[node][0]:
            explore(tree[node][0])
        if tree[node][1]:
            explore(tree[node][1])
    print(node)

sys.setrecursionlimit(10000)
tree = [False] * 1000001
root = int(input())
put(root, root)
while True:
    try:
        put(root, int(sys.stdin.readline()))
    except:
        break
explore(root)

