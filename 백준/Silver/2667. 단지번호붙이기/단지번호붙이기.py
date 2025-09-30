import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x,start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue=deque([(start_x,start_y)])
    pot[start_x][start_y]=0
    cnt = 1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
           
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if pot[nx][ny] == 1:
                pot[nx][ny] = 0
                queue.append((nx, ny))
                cnt+=1
    return cnt

n=int(input())
pot=[]
count=[]

for _ in range(n):
    x=input().rstrip()
    tmp=[]
    for y in x:
        tmp.append(int(y))
    pot.append(tmp)

for i in range(n):
    for j in range(n):
        if pot[i][j]==1:
            count.append(bfs(i,j))

count.sort()
print(len(count))
for i in count:
    print(i)