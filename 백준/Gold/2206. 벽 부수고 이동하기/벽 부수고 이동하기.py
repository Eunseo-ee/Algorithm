import sys
from collections import deque

input = sys.stdin.readline

#########################################################################
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs():
    q=deque([(1,1,0,1)]) # (x,y,broken, distance)
    visited[1][1][0]=True # broken=0 상태로 방문

    while q:
        x,y,broken,dist=q.popleft()

        if (y,x) == (n,m):
            return dist

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<nx<=m and 0<ny<=n:
                if graph[ny][nx]==0 and not visited[ny][nx][broken]:
                    visited[ny][nx][broken]=1
                    q.append((nx,ny,broken,dist+1))

                if graph[ny][nx]==1 and broken==0 and visited[ny][nx][1]==0: # 아직 벽 안 부숨
                    visited[ny][nx][1]=1
                    q.append((nx,ny,1,dist+1))
    return -1

n,m=map(int,input().split())
graph=[[0 for i in range(m+1)]]

for i in range(n):
    graph.append([0]+list(map(int,input().rstrip())))

visited = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]

ans=bfs()
if ans==-1:
    print(-1)
else:
    print(ans)