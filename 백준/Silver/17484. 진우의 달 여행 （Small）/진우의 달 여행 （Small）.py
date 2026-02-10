import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
road = []
dp = [[[0, 0, 0] for _ in range(m)]] + [
    [[float("inf"), float("inf"), float("inf")] for _ in range(m)] for _ in range(n)
]

for _ in range(n):
    road.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(m):
        # 바로 위, 오른쪽 위에 값만 비교 (왼쪽 위의 값 없음)
        if j < m - 1:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + road[i - 1][j]
        # 바로 위, 왼쪽 위에 값만 비교 (오른쪽 위의 값 없음)
        if 0 < j:
            dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + road[i - 1][j]
        # 전체 값 비교 가능
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + road[i - 1][j]

min_value = float("inf")
for row in dp[i]:
    for each in row:
        min_value = min(min_value, each)
print(min_value)
