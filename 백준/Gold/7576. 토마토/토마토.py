import sys
from collections import deque

input=sys.stdin.readline

###################################################################

m,n=map(int,input().split())
tomato=[]

for i in range(n):
    tomato.append(list(map(int,input().split())))

## 이미 다 익고 시작한 경우############################
flag=True
for i in range(n):
    if 0 not in tomato[i]:
        continue
    else:
        flag=False
        break

if flag:
    print(0)
    exit()
###################################################

dx=[0,0,-1,1]
dy=[1,-1,0,0]

q=deque([])

def bfs():
    while q:
        y,x=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=ny<n and 0<=nx<m and tomato[ny][nx]==0:
                tomato[ny][nx]=tomato[y][x]+1
                q.append((ny,nx))

ans=0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

bfs()

##########최종 답 출력################################
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans=max(ans, max(i))

print(ans-1)