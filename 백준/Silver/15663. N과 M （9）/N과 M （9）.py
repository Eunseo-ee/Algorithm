import sys
input = sys.stdin.readline

n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()
ans=[]

def dfs():
    check=0
    if len(ans) == m:
        print(*ans)
        return

    for i in range(n):
        if check!=num[i] and visited[i]==0:
            ans.append(num[i])
            visited[i]=True
            check=num[i]
            dfs()
            ans.pop()
            visited[i]=False

visited=[False]*(n+1)
dfs()