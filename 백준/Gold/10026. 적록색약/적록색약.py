import sys
input = sys.stdin.readline
from collections import deque
import heapq

import sys
input = sys.stdin.readline

n=int(input())
yes=[]
no=[]
yes_cnt=0
no_cnt=0

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

def bfs(start_x, start_y, color, graph):
    q=deque([(start_x, start_y)])
    graph[start_y][start_x]=0

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[ny][nx]==color:
                    q.append((nx, ny))
                    graph[ny][nx]=0

for _ in range(n):
    x=list(input().rstrip())
    no.append(x)
    tmp=[]
    for i in range(len(x)):
        if x[i]=='G':
            tmp.append('R')
        else:
            tmp.append(x[i])
    yes.append(tmp)

for i in range(n):
    for j in range(n):
        if no[i][j]!=0:
            bfs(j,i,no[i][j],no)
            no_cnt+=1
        if yes[i][j]!=0:
            bfs(j,i,yes[i][j],yes)
            yes_cnt+=1

print(no_cnt, yes_cnt)