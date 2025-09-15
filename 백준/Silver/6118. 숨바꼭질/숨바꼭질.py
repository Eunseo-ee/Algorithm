import sys
from collections import deque

input=sys.stdin.readline

###################################################################

n,m=map(int,input().split())
barn=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    barn[a].append(b)
    barn[b].append(a)

def bfs(v):
    q=deque([v])
    visited[v]=1

    while q:
        x=q.popleft()

        for i in barn[x]:
            if not visited[i]:
                visited[i]=visited[x]+1
                q.append(i)

visited=[0]*(n+1)
bfs(1)
mx=max(visited)

print(visited.index(mx), mx-1, visited.count(mx))