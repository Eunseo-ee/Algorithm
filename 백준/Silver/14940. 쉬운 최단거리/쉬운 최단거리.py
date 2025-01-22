from collections import deque

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(start_points):
    Q = deque(start_points)

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 지도 범위 내에서 탐색
            if 0 <= nx < m and 0 <= ny < n:
                # 아직 방문하지 않았고, 갈 수 있는 땅(1)인 경우
                if distance[ny][nx] == -1 and grid[ny][nx] == 1:
                    distance[ny][nx] = distance[y][x] + 1
                    Q.append((nx, ny))


# 입력 처리
n, m = map(int, input().split())  # n: 세로, m: 가로
grid = [list(map(int, input().split())) for _ in range(n)]

# 거리 배열 초기화
distance = [[-1 if grid[i][j] == 1 else 0 for j in range(m)] for i in range(n)]

# 목표 지점(2) 찾기
start_points = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_points.append((j, i))  # BFS 시작 지점
            distance[i][j] = 0  # 목표지점은 거리 0

# BFS 실행
bfs(start_points)

# 결과 출력
for row in distance:
    print(" ".join(map(str, row)))
