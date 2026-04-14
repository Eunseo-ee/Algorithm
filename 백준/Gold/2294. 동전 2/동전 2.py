import sys
input = sys.stdin.readline
from collections import deque
import heapq

import sys
input = sys.stdin.readline

n,k=map(int,input().split())
coin=[]
dp=[10001 for i in range(10001)]

for i in range(n):
    coin.append(int(input()))

coin.sort()

dp[0]=0

for x in coin:
    for i in range(x, k+1):
        # 현재 i 금액을 만드는 최소 개수 vs (i-coin)원 만든 개수 +1개
        if dp[i-x]!=10001:
            dp[i]=min(dp[i], dp[i-x]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])