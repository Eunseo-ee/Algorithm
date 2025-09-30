import sys
from collections import deque

input = sys.stdin.readline

###################################################################

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x1,y1):
    global cnt

    q=deque([(x1,y1)])
    twin[y1][x1]=0
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and twin[ny][nx]:
                twin[ny][nx]=0
                q.append((nx,ny))

graph = []
mx=0
ans=0

n = int(input())

for i in range(n):
    x = list(map(int, input().split()))
    graph.append(x)
    mx = max(max(x), mx)

for x in range(mx):
    twin=[[0]*n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>x:
                twin[i][j]=1
            else:
                twin[i][j]=0

    for i in range(n):
        for j in range(n):
            if twin[i][j]:
                bfs(j, i)
                tmp += 1

    ans=max(tmp,ans)

print(ans)