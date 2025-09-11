import sys

input=sys.stdin.readline

def dfs(v):

  for i in range(1,n+1):
    if num[v][i]==0:
      continue
    else:
      if visited[i]==0:
        visited[i]=1
        dfs(i)

n=int(input())

num=[0]
check=[[] for i in range(n+1)]
for _ in range(n):
  num.append([0]+list(map(int,input().split())))

visited = [0] * (n + 1)
for i in range(1,n+1):
  dfs(i)
  for j in range(1,n+1):
    if visited[j]==1:
      print(1, end=' ')
    else:
      print(0, end=' ')
  print()
  visited = [0] * (n + 1)