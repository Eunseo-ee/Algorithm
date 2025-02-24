import sys
from collections import deque
input=sys.stdin.readline

x=list(input().strip())
y=list(input().strip())

lx,ly=len(x),len(y)
cache=[0]*ly

for i in range(lx):
    cnt=0
    for j in range(ly):
        if cnt<cache[j]:
            cnt=cache[j]
        elif x[i]==y[j]:
            cache[j]=cnt+1

print(max(cache))