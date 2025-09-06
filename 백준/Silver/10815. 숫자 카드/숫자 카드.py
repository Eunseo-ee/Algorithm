import queue
import sys
from collections import deque

input=sys.stdin.readline

##############################################################################################

n=int(input())
card=sorted(list(map(int,input().split())))
m=int(input())
num=list(map(int,input().split()))

ans=[0 for i in range(m)]

for i in range(m):
    start,end=0,n-1
    while start<=end:
        mid = (start+end)//2
        if card[mid]==num[i]:
            ans[i]=1
            break
        elif card[mid]<num[i]:
            start=mid+1
        else:
            end=mid-1

print(*ans)