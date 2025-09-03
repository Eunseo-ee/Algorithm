import sys
input = sys.stdin.readline

n,m=map(int,input().split())
num=list(set(map(int,input().split())))
num.sort()
ans=[]

def dfs(start):
    if len(ans) == m:
        print(*ans)
        return

    for i in range(start,len(num)):
        ans.append(num[i])
        dfs(i)
        ans.pop()

dfs(0)