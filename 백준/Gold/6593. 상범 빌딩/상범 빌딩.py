import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


def bfs(start_x, start_y, start_z):
    visited = [[[float("inf") for i in range(c)] for i in range(r)] for i in range(l)]

    q = deque([(start_x, start_y, start_z)])
    visited[start_z][start_y][start_x] = 0

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and visited[nz][ny][nx]==float('inf'):
                if floor[nz][ny][nx] != "#":
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    q.append((nx, ny, nz))
                    if nz == end[2] and ny == end[1] and nx == end[0]:
                        return visited[nz][ny][nx]

    return -1


while True:
    l, r, c = map(int, input().split())
    floor = []
    start, end = [], []

    if l == 0 and r == 0 and c == 0:
        break

    for i in range(l):
        layer = []
        for j in range(r):
            x = list(input().rstrip())
            layer.append(x)
            if "S" in x:
                start = [x.index("S"), j, i]
            if "E" in x:
                end = [x.index("E"), j, i]
        floor.append(layer)
        temp = input()

    x = bfs(start[0], start[1], start[2])

    if x == -1:
        print("Trapped!")
        continue

    print(f"{"Escaped in "}{x}{" minute(s)."}")