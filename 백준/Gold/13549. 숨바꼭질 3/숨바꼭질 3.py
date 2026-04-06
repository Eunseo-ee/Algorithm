import sys
input = sys.stdin.readline
from collections import deque
import heapq

import sys
input = sys.stdin.readline

n,k=map(int,input().split())

# x+1, x-1,(1초) 2*x (0초)
visited=[-1]*100001

def bfs(n,k):
    queue=deque([n])
    visited[n]=0
    
    while True:
        x=queue.popleft()

        if x==k:
            return visited[k]

        nx = x * 2
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x]
            queue.appendleft(nx)
            
        for nx in (x - 1, x + 1):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
        

print(bfs(n,k))