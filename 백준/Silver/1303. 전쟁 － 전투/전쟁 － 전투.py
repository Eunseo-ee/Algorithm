import queue
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_x,start_y,color):
    Q=deque([(start_x,start_y)])
    global tmp

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    while Q:
        x,y=Q.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if man[ny][nx]==color:
                    Q.append((nx,ny))
                    tmp+=1
                    man[ny][nx]=0
                else:
                    continue
    return -1

n,m=map(int,input().split())
man=[]
for _ in range(m):
    man.append(list(input().rstrip()))

cnt_W,cnt_B=0,0
for i in range(m):
    for j in range(n):
        if man[i][j]==0:
            continue
        elif man[i][j]=='W':
            tmp = 0
            bfs(j,i,'W')
            if tmp == 0: tmp = 1
            cnt_W+=tmp**2

        elif man[i][j]=='B':
            tmp = 0
            bfs(j,i,'B')
            if tmp == 0: tmp = 1
            cnt_B+=tmp**2

print(cnt_W,cnt_B)