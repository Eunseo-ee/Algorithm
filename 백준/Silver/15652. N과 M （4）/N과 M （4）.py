n,m=map(int,input().split())

def dfs(start):
    if len(num)==m:
        print(' '.join(map(str,num)))
        return
    for i in range(start,n+1):
        if visited[i]==True:
            continue
        num.append(i)
        # visited[i]=True
        dfs(i)
        num.pop()
        # visited[i]=False

num=[]
visited=[False]*(n+1)
dfs(1)