import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())
box=[] # z,y,x

for i in range(h):
    box.append([])
    for j in range(n):
        box[i].append(list(map(int,input().split())))

Q=deque() # z,y,x

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x]==1:
                Q.append([z,y,x])

dx=[0,0,0,0,-1,1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]

while Q:
    length=len(Q)

    for _ in range(length):
        z,y,x=Q.popleft()

        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]

            if 0<=nx<m and 0<=ny<n and 0<=nz<h and box[nz][ny][nx]==0:
                box[nz][ny][nx]=box[z][y][x]+1
                Q.append([nz,ny,nx])

day=0

for tray in box:
    for row in tray:
        for tomato in row:
            if tomato==0:
                print(-1)
                exit(0)
        day=max(day,max(row))

print(day-1)