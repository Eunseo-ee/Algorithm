import sys
input=sys.stdin.readline

t=int(input())

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y):
    queue=[(x,y)]
    pot[x][y]=0

    while queue:
        x,y=queue.pop(0)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue

            if pot[nx][ny]==1:
                queue.append((nx,ny))
                pot[nx][ny]=0

for i in range(t):
    m,n,k=map(int,input().split())
    pot=[[0 for col in range(n)] for row in range(m)]
    cnt=0

    for j in range (k):
        x,y=map(int,input().split())
        pot[x][y]=1

    for a in range(m):
        for b in range(n):
            if pot[a][b]==1:
                bfs(a,b)
                cnt+=1

    print(cnt)