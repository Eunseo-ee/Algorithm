import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

nodes = list(map(int, input().split()))
delete = int(input())

root = nodes.index(-1)

tree = [[] for i in range(n)]
visited = [0 for i in range(n)]

for i in range(len(nodes)):
    if i == root:
        continue
    tree[nodes[i]].append(i)


def dfs(curr):
    if curr == delete:
        return 0

    leaf_cnt = 0
    child = 0  # 실제 탐색 가능한 자식의 수

    for neighbor in tree[curr]:
        if neighbor == delete:
            continue

        child += 1
        leaf_cnt += dfs(neighbor)

    if child == 0:
        return 1

    return leaf_cnt


if root == delete:
    print(0)
else:
    print(dfs(root))