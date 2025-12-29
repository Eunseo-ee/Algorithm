import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 0=북, 1=동, 2=남, 3=서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = c, r
ans = 0

while True:
    # 1. 현재 칸 청소
    if board[y][x] == 0:
        board[y][x] = 2
        ans += 1

    # 2. 주변에 청소 안 된 칸 있는지
    found = False
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 회전
        nx = x + dy[d]
        ny = y + dx[d]
        if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 0:
            x, y = nx, ny
            found = True
            break

    if found:
        continue

    # 3. 뒤로 이동
    back_dir = (d + 2) % 4
    bx = x + dy[back_dir]
    by = y + dx[back_dir]

    if 0 <= bx < m and 0 <= by < n and board[by][bx] != 1:
        x, y = bx, by
    else:
        break

print(ans)
