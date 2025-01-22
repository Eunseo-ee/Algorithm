import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = []
dp = [[0 for i in range(n)] for j in range(n)]
dp[0][0] = 1

for i in range(n):
    num.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if num[i][j] == 0 or dp[i][j]==0:
            continue

        if i + num[i][j] < n:
            dp[i + num[i][j]][j] += dp[i][j]

        if j + num[i][j] < n:
            dp[i][j + num[i][j]] += dp[i][j]

print(dp[n - 1][n - 1])