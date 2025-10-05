import copy
import sys
from collections import deque

input = sys.stdin.readline

#########################################################################

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(start_x, start_y, cnt):

    q=deque([(start_x, start_y)])
    graph[start_y][start_x] = -1
    tmp[start_y][start_x] = cnt + 1

    while q:
        x,y=q.popleft()
        is_edge = False

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[ny][nx]==0:
                is_edge = True
            elif 0<=nx<n and 0<=ny<n and graph[ny][nx]==1:
                graph[ny][nx] = -1
                tmp[ny][nx] = cnt + 1
                q.append((nx, ny))
        if is_edge:
            land[cnt].append((x, y))

def bfs_length(start_x, start_y, num):
    global ans
    q=deque([(start_x, start_y, 0)])
    visited=[[0 for i in range(n)] for _ in range(n)]
    visited[start_y][start_x] = 1

    while q:
        x,y,dist=q.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and visited[ny][nx]!=1:
                visited[ny][nx] = 1
                if tmp[ny][nx]==0:
                    q.append((nx,ny,dist+1))
                elif tmp[ny][nx]!=num:
                    ans=min(ans, dist)
                    return

n=int(input())
graph=[]
cnt=0
land=[]
ans=1000000

tmp = [[0]*n for _ in range(n)]

# 0 : 바다, 1 : 육지
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            land.append([])
            bfs(j,i, cnt)
            cnt += 1

for i in range(len(land)):
    for j in range(len(land[i])):
        x,y=land[i][j]
        bfs_length(x,y,tmp[y][x])

print(ans)