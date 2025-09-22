import sys
from collections import deque

input=sys.stdin.readline

###################################################################

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def bfs(start_x, start_y, n):
    q=deque([(start_x, start_y, 0)])
    visited=set([start_x, start_y])
    cnt=0

    while q:
        x,y, cnt=q.popleft()

        if x == end_x and y == end_y:
            return cnt

        for i in range(8):
            nx,ny=x+dx[i], y+dy[i]

            if 0 <= nx < l and 0 <= ny < l and (nx, ny) not in visited:
                q.append((nx, ny, cnt + 1))
                visited.add((nx, ny))

    return -1

t=int(input())

for i in range(t):
    l=int(input())

    start_x, start_y=map(int,input().split())
    end_x, end_y=map(int,input().split())

    if start_x==end_x and start_y==end_y:
        print(0)
        continue

    cnt=0
    print(bfs(start_x, start_y, 0))