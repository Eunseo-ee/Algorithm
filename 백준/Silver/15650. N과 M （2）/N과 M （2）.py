n,m=map(int,input().split())

def dfs():
    if len(num)==m and sorted(num)==num:
        print(' '.join(map(str,num)))
        return
    for i in range(1,n+1):
        if visited[i]==True:
            continue
        num.append(i)
        visited[i]=True
        dfs()
        num.pop()
        visited[i]=False

num=[]
visited=[False]*(n+1)
dfs()