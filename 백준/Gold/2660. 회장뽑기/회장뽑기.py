import sys
from collections import deque

input=sys.stdin.readline

###################################################################

n=int(input())
link=[[] for i in range(n+1)]

while True:
    a,b=map(int,input().split())

    if a==-1 and b==-1 : break

    link[a].append(b)   
    link[b].append(a)

def bfs(v):
    q=deque([v])

    while q:
        x=q.popleft()
        for i in link[x]:
            if not visited[i] and i!=v:
                q.append(i)
                visited[i]=visited[x]+1

ans=[]

for i in range(1,n+1):
    visited = [0] * (n + 1)
    bfs(i)
    ans.append(max(visited))

mn=min(ans)

print(mn, ans.count(mn))
for i in range(n):
    if ans[i]==mn:
        print(i+1, end=' ')