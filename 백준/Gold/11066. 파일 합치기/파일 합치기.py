import sys
from collections import deque

input = sys.stdin.readline

#########################################################################

for _ in range(int(input())):
    n=int(input())
    chap=list(map(int,input().split()))

    # 누적합 (prefix sum)
    prefix=[0]*(n+1)
    for i in range(1,n+1):
        prefix[i]=prefix[i-1]+chap[i-1]

    dp=[[0 for i in range(n+1)] for j in range(n+1)]

    dp[0][0]=chap[0]

    # 구간 길이 len = 2 ~ n
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            # i~j 사이에서 분할 위치 k
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (prefix[j] - prefix[i - 1])
                dp[i][j] = min(dp[i][j], cost)

    print(dp[1][n])