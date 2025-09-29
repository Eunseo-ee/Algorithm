import sys
from collections import deque
input = sys.stdin.readline

# 이동 방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y):
    global cnt
    queue = deque([(start_x, start_y)])
    dot[start_y][start_x] = 1  # 방문 처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 유효한 범위 내에 있고, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and dot[ny][nx] == 0:
                dot[ny][nx] = 1
                queue.append((nx, ny))
                cnt += 1

m, n, k = map(int, input().split())
dot = [[0 for _ in range(n)] for _ in range(m)]  # 정확한 크기로 초기화
square = []

# 사각형 영역 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            dot[j][i] = 1

# BFS 탐색
for i in range(m):
    for j in range(n):
        if dot[i][j] == 0:
            cnt = 1
            bfs(j, i)  # BFS 호출
            square.append(cnt)

# 결과 출력
square.sort()
print(len(square))  # 영역의 개수
print(*square)
