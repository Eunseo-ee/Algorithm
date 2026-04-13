import sys
input = sys.stdin.readline
from collections import deque
import heapq
import math

import sys
input = sys.stdin.readline

for i in range(int(input())):
    x,y=map(int,input().split())

    d=y-x
    n=int(math.sqrt(d))
    rest=d-n*n

    if rest==0:
        cnt=2*n-1
    elif 0<=rest<=n: # 속도 n까지 낼 수 있으니까 나은 거리가 n 이하면 숫자 하나만 끼워넣어도 됨
        cnt=2*n
    else: # 숫자 두개 써서 해야함
        cnt=2*n+1

    print(cnt)