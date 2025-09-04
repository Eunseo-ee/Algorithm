import sys

input = sys.stdin.readline

def dfs(depth,idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, k):
        out.append(s[i])
        dfs(depth+1,i+1)
        out.pop()

while True:
    s=list(map(int,input().split()))
    if len(s)==1:
        break
    k=s.pop(0)

    out=[]
    dfs(0,0)
    print()