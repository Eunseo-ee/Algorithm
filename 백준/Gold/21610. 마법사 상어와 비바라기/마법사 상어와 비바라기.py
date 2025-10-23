import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

n, m = map(int, input().split())
a = []
# 초기 비구름 위치
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    d, s = map(int, input().split())
    prev_len = len(cloud)
    # 이전에 구름 제거된 위치
    ex_cloud = set()
    new_cloud = set()

    # 1. 이동
    for y, x in cloud:
        ny = (y + dy[d] * s) % n
        nx = (x + dx[d] * s) % n

        new_cloud.add((ny, nx))

    cloud = new_cloud

    # 2. 물 늘리기
    for y, x in cloud:
        a[y][x] += 1

    # 3. 구름 없애고 4. 대각선 방향 칸에도 물 추가
    for y, x in cloud:
        ex_cloud.add((y, x))

        cnt = 0
        for step in [2, 4, 6, 8]:
            nx, ny = x + dx[step], y + dy[step]

            if (
                0 <= nx < n and 0 <= ny < n and a[ny][nx] != 0
            ):  # 대각선 칸에 물이 0 이 아니면
                cnt += 1
        a[y][x] += cnt

    cloud = []

    # 5. 물2이상인 칸에 구름 생기기
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2 and (i, j) not in ex_cloud:
                cloud.append((i, j))
                a[i][j] -= 2

ans = 0
for i in range(n):
    ans += sum(a[i])

print(ans)
