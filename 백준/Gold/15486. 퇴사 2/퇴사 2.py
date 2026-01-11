import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# T= 기간 P = 요금

n = int(input())
t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 2)
current_max = 0  # i일 전까지의 최대 수익을 계속 보관

for i in range(1, n + 1):
    current_max = max(current_max, dp[i])

    finish_day = i + t[i - 1]

    if finish_day <= n + 1:
        # 상담이 끝나는 날의 수익 = max(기존 기록, 현재 최대 수익 + 상담비)
        dp[finish_day] = max(dp[finish_day], current_max + p[i - 1])

print(max(current_max, dp[n + 1]))