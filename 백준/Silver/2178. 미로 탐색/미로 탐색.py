import sys
from collections import deque

input=sys.stdin.readline

###################################################################
dx=[0,0,-1,1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def bfs(start_y, start_x, graph):
    q=deque([(start_y, start_x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                q.append((ny, nx))
                graph[ny][nx]=graph[y][x] + 1
    return graph[n-1][m-1]

print(bfs(0,0,graph))