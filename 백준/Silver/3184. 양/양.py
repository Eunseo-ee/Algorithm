import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x,y):
    if -1>=x or x>=r or -1>=y or y>=c:
        return False
    if cage[x][y]!='#':
        if cage[x][y]=='o':
            o.append(1)
        elif cage[x][y]=='v':
            v.append(1)
        cage[x][y]='#'

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)

        return True
    return False

r,c=map(int,input().split())
cage=[]
sheep,wolf=0,0

# o : 양 v : 늑대 # :울타리 . : 0빈 곳
for i in range(r):
    cage.append(list(input()))

for i in range(r):
    for j in range(c):
        if cage[i][j]!='#':
            o = []
            v = []
            dfs(i,j)

            if len(v)>=len(o):
                wolf+=len(v)
            else:
                sheep +=len(o)

print(sheep,wolf)