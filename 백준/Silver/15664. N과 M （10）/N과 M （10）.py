import sys
input = sys.stdin.readline

n,m=map(int,input().split())

a=sorted(list(map(int,input().split())))

def dfs(start):
    if len(tmp)==m:
        print(*tmp)
        return
    former=0
    for i in range(start,len(a)):
        if a[i]!=former:
            tmp.append(a[i])
            former=a[i]
        else:
            continue
        dfs(i+1)
        tmp.pop()

tmp=[]
dfs(0)
