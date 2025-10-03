import sys
from collections import deque
import heapq

input = sys.stdin.readline

###################################################################

n=int(input())
heap=[]

for i in range(n):
    heapq.heappush(heap, int(input()))

tmp=0
ans=0

while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    s=a+b
    ans+=s
    heapq.heappush(heap,s)

print(ans)