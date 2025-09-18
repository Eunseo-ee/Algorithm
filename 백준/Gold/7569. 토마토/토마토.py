import sys
from collections import deque

input=sys.stdin.readline

###################################################################

m,n,h=map(int,input().split())
tomato=[]

tomato = []
for _ in range(h):
    layer = [list(map(int,input().split())) for _ in range(n)]
    tomato.append(layer)   # tomato[z][y][x] 가능

## 이미 다 익고 시작한 경우############################
flag = True
for z in range(h):
    for y in range(n):
        if 0 in tomato[z][y]:
            flag = False
            break

if flag:
    print(0)
    exit()
###################################################

# 상 하 좌 우 위 아래
dx=[0,0,-1,1, 0, 0]
dy=[1,-1,0,0, 0, 0]
dz=[0, 0, 0, 0, 1, -1]

q=deque([])

def bfs():
    while q:
        z, y,x=q.popleft()
        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
            if 0<=ny<n and 0<=nx<m and 0<=nz<h and tomato[nz][ny][nx]==0:
                tomato[nz][ny][nx]=tomato[z][y][x]+1
                q.append((nz,ny,nx))

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                q.append([k, i, j])

bfs()

##########최종 답 출력################################
ans = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 0:
                print(-1)
                exit()
        ans = max(ans, max(tomato[z][y]))

print(ans-1)