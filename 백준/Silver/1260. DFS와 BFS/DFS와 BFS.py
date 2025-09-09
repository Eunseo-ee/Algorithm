import queue
import sys
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(100000)

##############################################################################################

n,m,v=map(int,input().split())
dot=[[] for i in range(n+1)]

for i in range(m):
    u,k=map(int,input().split())
    dot[u].append(k)
    dot[k].append(u)

for i in range(1, n + 1):
    dot[i].sort()

def dfs(dot, v, visited):
    visited[v]=True
    print(v, end=" ")

    for i in dot[v]:
        if not visited[i]:
            dfs(dot, i, visited)

def bfs(dot, v, visited):
    q=deque([v])
    visited[v]=True

    while q:
        x=q.popleft()
        print(x, end=" ")
        for i in dot[x]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

visited=[False] * (n+1)
dfs(dot,v,visited)
print()
visited=[False] * (n+1)
bfs(dot,v,visited)