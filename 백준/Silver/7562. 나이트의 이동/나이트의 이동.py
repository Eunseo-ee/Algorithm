import sys
from collections import deque
input = sys.stdin.readline

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

tmp=1000000000000

def bfs(x1, y1, x2, y2, n):
    queue=deque([(x1,y1,0)])
    visited = set([(x1, y1)])
    cnt=0

    while queue:
        x,y,cnt=queue.popleft()

        if x==x2 and y==y2:
            return cnt

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,cnt+1))
    return -1


t=int(input())

for _ in range(t):
    n=int(input())
    x1,y1=map(int,input().split()) # start
    x2,y2=map(int,input().split()) # departure

    if x1==x2 and y1==y2:
        print(0)
        continue

    print(bfs(x1, y1, x2, y2, n))