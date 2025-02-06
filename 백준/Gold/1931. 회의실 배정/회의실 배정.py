import queue
import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
time=[]

endPoint: int=0
ans:int=0

for i in range(n):
    time.append(list(map(int,input().split())))

time.sort(key=lambda x:(x[1],x[0]))

for newStart, newEnd in time:
    if endPoint<=newStart:
        ans+=1
        endPoint=newEnd
        
print(ans)