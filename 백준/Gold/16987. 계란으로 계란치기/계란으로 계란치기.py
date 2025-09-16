import sys
from collections import deque

input=sys.stdin.readline

###################################################################

n=int(input())
egg=[]
# 내구도, 무게

for i in range(n):
    egg.append(list(map(int,input().split())))

def dfs(v):
    global ans

    if v==n:
        total=0
        for i in range(n):
            if egg[i][0]<=0:
                total+=1

        ans=max(ans, total)
        return

    if egg[v][0]<=0:
        dfs(v+1)
        return

    check=True

    for i in range(n):
        if i==v:
            continue
        if egg[i][0]>0:
            check=False
            break

    if check: # 다 깨져있는 경우
        ans=max(ans, n-1)
        return

    for i in range(n):
        if i==v or egg[i][0]<=0:
            continue
        egg[v][0]-=egg[i][1]
        egg[i][0]-=egg[v][1]
        dfs(v+1)
        egg[v][0]+=egg[i][1]
        egg[i][0]+=egg[v][1]

ans=0
dfs(0)
print(ans)