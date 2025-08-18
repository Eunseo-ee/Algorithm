import queue
import sys
from collections import deque

input=sys.stdin.readline

##############################################################################################

dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
campus=[]
x,y=0,0
ans=0

for i in range(n):
    campus.append(input())
    for j in range(m):
        if campus[i][j]=='I':
            x,y=i,j

visited=[[0] * m for _ in range(n)]

deq=deque()
deq.append([x,y])

while deq:
    x,y=deq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            visited[nx][ny]=1
            if campus[nx][ny]=='O':
                deq.appendleft([nx,ny])
            elif campus[nx][ny]=='P':
                deq.appendleft([nx,ny])
                ans+=1

print('TT' if ans==0 else ans)