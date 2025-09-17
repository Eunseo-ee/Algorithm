import sys
from collections import deque

input=sys.stdin.readline

###################################################################
dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
art=[]

def bfs(start_y, start_x, graph):
    global tmp
    tmp = 1
    q=deque([(start_y, start_x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                q.append((ny, nx))
                graph[ny][nx]=0
                tmp+=1
    return tmp

for i in range(n):
    art.append(list(map(int,input().split())))

ans=0
cnt=0

for i in range(n):
    for j in range(m):
        if art[i][j]==1:
            art[i][j]=0
            tmp=bfs(i,j,art)
            ans=max(ans,tmp)
            cnt+=1

print(cnt)
print(ans)