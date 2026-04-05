import sys
input = sys.stdin.readline
from collections import deque
import heapq

import sys
input = sys.stdin.readline

dx=[0,0,0,0,-1,1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]

def bfs():
    q=deque(tomato)

    while q:
        x,y,z=q.popleft()

        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]

            if 0<=nx<m and 0<=ny<n and 0<=nz<h and box[nz][ny][nx]==0:
                box[nz][ny][nx]=box[z][y][x]+1
                q.append((nx,ny,nz))

m,n,h = map(int,input().split())
box=[]
tomato=[]

for j in range(h):
    layer=[]
    for k in range(n):
        x=list(map(int,input().split()))
        for i in range(len(x)):
            if x[i]==1:
                tomato.append((i, k, j))
        layer.append(x)
    box.append(layer)

bfs()

mx = 0
for z in range(h):
    for y in range(n):
        if 0 in box[z][y]: # 익지 않은 토마토 체크
            print(-1)
            sys.exit()
        # 한 줄(row)에서 가장 큰 값을 찾아 mx와 비교
        mx = max(mx, max(box[z][y]))

print(mx - 1)