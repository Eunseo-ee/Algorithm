import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)   # b -> a (b를 해킹하면 a 해킹 가능)

def bfs(start):
    visited = [0] * (n+1)
    q = deque([start])
    visited[start] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for nxt in graph[x]:
            if not visited[nxt]:
                visited[nxt] = 1
                cnt += 1
                q.append(nxt)
    return cnt

ans = [0] * (n+1)
mx = 0

for i in range(1, n+1):
    ans[i] = bfs(i)
    mx = max(mx, ans[i])

for i in range(1, n+1):
    if ans[i] == mx:
        print(i, end=' ')
