import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and tmp[ny][nx] == 0:
                q.append((nx, ny))
                tmp[ny][nx] = 2


n, m = map(int, input().split())
graph = []
not_wall = []
virus = []

# 0:빈 칸 1:벽 2:바이러스가 있는 위치
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        if x[j] == 0:
            not_wall.append((i, j))
        elif x[j] == 2:
            virus.append((i, j))
    graph.append(x)

crack = combinations(not_wall, 3)
ans = 0

for step in crack:
    tmp = [row[:] for row in graph]  # 원본 복사
    for y, x in step:
        tmp[y][x] = 1
    for y, x in virus:
        bfs(x, y)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)

print(ans)