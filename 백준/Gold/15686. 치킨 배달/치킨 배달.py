import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx,dy=[0,0,-1,1],[1,-1,0,0]

def length(x,y,comb):
    ans=float('inf')

    for i in comb:
        tmp=abs(i[1]-x)+abs(i[0]-y)
        ans=min(ans,tmp)

    return ans

n,m=map(int,input().split())
graph=[]
ans=10000000
chicken=[]
house=[]

for i in range(n):
    x=list(map(int,input().split()))

    for j in range(n):
        if x[j]==2: # 치킨집
            chicken.append((i,j))
        elif x[j]==1: # 집
            house.append((i,j))
    graph.append(x)
# 0 : 빈칸 1 : 집 2 : 치킨집

step=list(combinations(chicken,m))
compare=[]

for i in range(len(step)):
    tmp_ans=0
    for y,x in house:
        tmp_ans+=length(x,y,step[i])
    compare.append(tmp_ans)

print(min(compare))