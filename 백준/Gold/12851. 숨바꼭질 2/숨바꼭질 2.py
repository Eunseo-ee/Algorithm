import sys
from collections import deque

input = sys.stdin.readline

#########################################################################
n,k=map(int,input().split())

# x+1, x-1, 2*x

def bfs():
    global cnt
    q=deque()
    q.append(n)

    visited[n]=0
    cnt[n]=1

    while q:
        x=q.popleft()

        for nx in ([x+1, x-1, 2*x]):
            if 0<=nx<=100000:
                # 처음 방문
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    cnt[nx]=cnt[x]
                    q.append(nx)

                # 같은 거리로 다시 도착한 경우 -> 경로 누적
                elif visited[nx]==visited[x]+1:
                    cnt[nx]+=cnt[x]

visited=[-1 for i in range(100001)]
cnt=[0]*(100001)

bfs()

print(visited[k])
print(cnt[k])