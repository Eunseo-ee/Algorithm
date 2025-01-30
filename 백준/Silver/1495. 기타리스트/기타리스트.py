import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    global cnt
    Q=deque([(s,0)])
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[0][s] = True  # 시작 볼륨은 방문 처리
    max_volume = -1

    while Q:
        volume, song=Q.popleft()

        if song == n:  # 마지막 곡을 연주했다면 최댓값을 갱신
            max_volume = max(max_volume, volume)
            continue  # 더 이상 탐색할 필요 없음

        for change in [v[song], -v[song]]:  # 현재 곡에서 ± 가능
            new_volume = volume + change
            if 0 <= new_volume <= m and not visited[song + 1][new_volume]:
                visited[song + 1][new_volume] = True
                Q.append((new_volume, song + 1))

    return max_volume

n,s,m=map(int,input().split())
v=list(map(int,input().split()))
num=[]
cnt=0

result = bfs()
print(result if result != -1 else -1)