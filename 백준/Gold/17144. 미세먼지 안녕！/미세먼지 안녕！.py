import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c, t = map(int, input().split())
a = []  # 방 상태
air = []  # 공기청정기 행 위치

for i in range(r):
    row = list(map(int, input().split()))
    if row[0] == -1:
        air.append(i)
    a.append(row)

def spread():
    temp = [[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if a[y][x] > 0:
                amount = a[y][x] // 5
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < c and 0 <= ny < r and a[ny][nx] != -1:
                        temp[ny][nx] += amount
                        cnt += 1
                a[y][x] -= amount * cnt

    # 확산 결과 반영
    for y in range(r):
        for x in range(c):
            a[y][x] += temp[y][x]

def circulate():
    top, bottom = air

    # 위쪽 (반시계)
    for i in range(top-1, 0, -1):
        a[i][0] = a[i-1][0]
    for i in range(c-1):
        a[0][i] = a[0][i+1]
    for i in range(top):
        a[i][c-1] = a[i+1][c-1]
    for i in range(c-1, 1, -1):
        a[top][i] = a[top][i-1]
    a[top][1] = 0

    # 아래쪽 (시계)
    for i in range(bottom+1, r-1):
        a[i][0] = a[i+1][0]
    for i in range(c-1):
        a[r-1][i] = a[r-1][i+1]
    for i in range(r-1, bottom, -1):
        a[i][c-1] = a[i-1][c-1]
    for i in range(c-1, 1, -1):
        a[bottom][i] = a[bottom][i-1]
    a[bottom][1] = 0

    a[top][0] = -1
    a[bottom][0] = -1

for _ in range(t):
    spread()
    circulate()

ans = 0
for i in range(r):
    for j in range(c):
        if a[i][j] > 0:
            ans += a[i][j]
print(ans)