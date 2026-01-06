import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, r, q = map(int, input().split())
line = [[] for i in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

dp = [0] * (n + 1)
visited = [False] * (n + 1)


def cnt_subtree_nodes(curr):
    visited[curr] = True
    dp[curr] = 1  # 일단 자기 자신(노드1개)으로 초기화

    for neighbor in line[curr]:
        if not visited[neighbor]:
            cnt_subtree_nodes(neighbor)
            dp[curr] += dp[neighbor]


cnt_subtree_nodes(r)

for i in range(q):
    u = int(input())

    print(dp[u])