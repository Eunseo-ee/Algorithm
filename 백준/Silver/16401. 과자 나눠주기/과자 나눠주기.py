import queue
import sys
from collections import deque

input=sys.stdin.readline

###################################################################

m,n=map(int,input().split())

l=list(map(int,input().split()))

start, end=1,max(l)
ans=0

while start<=end:
    mid=(start+end)//2

    cnt=0

    for i in l:
        if i<mid:
            continue
        else:
            cnt+=i//mid

    if cnt>=m:
        start=mid+1
        ans=mid
    else:
        end=mid-1

print(ans)