n,m=map(int,input().split())
prob=list(map(int,input().split()))

prob.sort()

def dfs(start):
    if len(num)==m:
        print(' '.join(map(str,num)))
        return
    for i in range(start,n):
        if visited[i]==True:
            continue
        num.append(prob[i])
        # visited[i]=True
        dfs(i)
        num.pop()
        # visited[i]=False

num=[]
visited=[False]*(n+1)
dfs(0)