import queue
import sys
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(100000)

##############################################################################################
def dfs(com, v, visited, depth):
    global cnt

    if depth==2:
        return

    for i in com[v]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
        dfs(com, i, visited, depth+1)

n=int(input())
m=int(input())

com=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    com[a].append(b)
    com[b].append(a)

visited=[False]*(n+1)
cnt=0
dfs(com, 1, visited, 0)
if cnt==0:print(cnt)
else:
    print(cnt-1)    