import sys
from collections import deque
input = sys.stdin.readline

k=int(input())
signs=list(input().split())
visited = [0]*10
ans=[]

def check(a,b,op):
    if op=='>':
        if a<b:return False
    if op=='<':
        if a>b:return False
    return True

# 최대, 최소
def dfs (cnt,num):
    if cnt==k+1:
        ans.append(num)
        return
    for i in range(10):
        if visited[i]: continue
        
        if cnt==0 or check(num[cnt-1],str(i),signs[cnt-1]):
            visited[i]=1
            dfs(cnt+1,num+str(i))
            visited[i]=0

dfs(0, '')
ans.sort()
print(ans[-1])
print(ans[0])