import sys
from collections import deque
import heapq

input = sys.stdin.readline

# 접시수,초밥가짓수,연속접시수,쿠폰번호
n,d,k,c=map(int,input().split())
cir=[]

M=0

for _ in range(n):
    cir.append(int(input()))

for i in range(len(cir)):
    if i<=n-k:
        tmp=set(cir[i:i+k])
    else:
        tmp=set(cir[i:])
        tmp.update(cir[:(i+k)%n])
    tmp.add(c)
    M=max(M,len(tmp))

print(M)