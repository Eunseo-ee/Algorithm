import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if visited[ny][nx] == -1:  # 아직 방문 X
                # 벽 없으면
                if graph[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x]
                    # 여기가 포인트!! 벽이 없는 곳을 우선으로 돌도록 큐 맨 왼쪽으로
                    q.appendleft([nx, ny])
                # 벽 있으면
                else:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([nx, ny])  # 큐 맨 오른쪽에 추가


m, n = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().strip())))

# 벽 깬 횟수
visited = [[-1 for i in range(m)] for j in range(n)]

bfs(0, 0)
print(visited[n - 1][m - 1])
