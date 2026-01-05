import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
dist=[[] for i in range(n+1)]

for i in range(n-1):
    s,e,d=map(int,input().split())
    dist[s].append([e,d])
    dist[e].append([s,d])

for i in range(m):
    start,end=map(int,input().split())

    q=deque()
    for i in dist[start]:
        q.append((i[0],i[1]))

    visited=[False]*(n+1)
    visited[start]=True

    while q:
        tmp,tmp_d=q.popleft()
        
        if tmp==end:
            print(tmp_d)
            break

        for i in dist[tmp]:
            if not visited[i[0]]:
                visited[i[0]]=True
                q.append((i[0],tmp_d+i[1]))