import itertools
import sys
from collections import deque
input=sys.stdin.readline

def length(x,y, comp):
    ans=float('inf')
    for i in comp:
        tmp=abs(i[1]-x)+abs(i[0]-y)
        ans=min(tmp,ans)
    return ans

# 0: none 1 : 집 2 : 치킨집

n,m=map(int,input().split())
chk=[]
combi=[]

for i in range(n):
    now=list(map(int,input().split()))
    for j in range(n):
        if now[j]==2:
            combi.append([i,j])
    chk.append(now)

if len(combi)>m:
    combi=list(itertools.combinations(combi, m))
    compare = []
    for i in range(len(combi)):
        tmp = 0
        for x in range(n):
            for y in range(n):
                if chk[y][x] == 1:
                    tmp += length(x, y, combi[i])
        compare.append(tmp)
else:
    compare = []
    tmp = 0
    for x in range(n):
        for y in range(n):
            if chk[y][x]==1:
                tmp += length(x, y, combi)
    compare.append(tmp)

print(min(compare))