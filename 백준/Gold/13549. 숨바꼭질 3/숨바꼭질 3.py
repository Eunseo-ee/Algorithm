import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs(start):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        dx = [-1, 1, x]

        if x == k:
            return visited[x]

        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx <= 100000 and (visited[nx] == -1 or visited[nx] > visited[x]):
                if i == 2:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    return 0


n, k = map(int, input().split())

visited = [-1 for i in range(100001)]

visited[n] = 0
bfs(n)
print(visited[k])