import queue
import sys
from collections import deque

input=sys.stdin.readline

##############################################################################################

t=int(input())

for _ in range(t):
    a=list(map(int,input().split()))
    a=sorted(a)
    print(a[-3])