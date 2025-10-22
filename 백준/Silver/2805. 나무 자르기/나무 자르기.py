import sys
from collections import deque

input = sys.stdin.readline

#########################################################################

n,m=map(int,input().split())

tree=list(map(int,input().split()))

mx=max(tree)

start=1
end=mx

while start<=end:
    mid=(start+end)//2

    tmp=0
    for tr in tree:
        if tr>=mid:
            tmp+=tr-mid

    if tmp>=m:
        start=mid+1
    else:
        end=mid-1

print(end)