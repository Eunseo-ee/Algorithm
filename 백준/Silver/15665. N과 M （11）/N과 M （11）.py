import sys
input = sys.stdin.readline

n,m=map(int,input().split())

a=sorted(list(map(int,input().split())))

def dfs():
    if len(tmp)==m:
        print(*tmp)
        return
    former=0
    for i in range(0,len(a)):
        if a[i]!=former:
            tmp.append(a[i])
            former=a[i]
        else:
            continue
        dfs()
        tmp.pop()

tmp=[]
dfs()
