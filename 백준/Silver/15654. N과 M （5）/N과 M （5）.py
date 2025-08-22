n,m=map(int,input().split())
prob=list(map(int,input().split()))

prob.sort()

def dfs():
    if len(num)==m:
        print(' '.join(map(str,num)))
        return
    for i in range(n):
        if visited[i]==True:
            continue
        num.append(prob[i])
        visited[i]=True
        dfs()
        num.pop()
        visited[i]=False

num=[]
visited=[False]*(n+1)
dfs()