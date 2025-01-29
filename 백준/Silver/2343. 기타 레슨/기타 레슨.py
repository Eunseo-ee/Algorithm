import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
len=list(map(int,input().split()))

start=max(len)
end=sum(len)

while start<=end:
    mid=(start+end)//2

    total=0
    cnt=1

    for t in len:
        if total+t>mid:
            cnt+=1
            total=0
        total+=t

    if cnt<=m:
        ans=mid
        end=mid-1

    else:
        start=mid+1
        
print(ans)