import sys
from collections import deque
import copy

input = sys.stdin.readline

###################################################################

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(start):
    if len(s) == 3:
        check.append(s[:])
        return

    for i in range(start, len(empty)):
        s.append(empty[i])
        dfs(i + 1)
        s.pop()


def bfs(start_x, start_y):
    q=deque([(start_x, start_y)])

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0:
                visited[ny][nx]=2
                q.append((nx,ny))

n, m = map(int, input().split())
graph = []
empty = []
virus=[]
s = []
check = []  # dfs 돌려서 찾은 조합들

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        if graph[i][j]==2:
            virus.append((i, j))

ans=0
dfs(0)  # 빈칸들 다 확인

for i in range(len(check)):
    visited=copy.deepcopy(graph)
    tmp=0

    for j in range(3):
        y,x=check[i][j]
        visited[y][x]=1

    for y,x in virus:
        bfs(x,y)

    for j in range(n):
        tmp+=visited[j].count(0)

    ans=max(ans,tmp)

print(ans)