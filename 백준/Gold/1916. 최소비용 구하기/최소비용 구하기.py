import sys
input = sys.stdin.readline
import heapq

n=int(input())
m=int(input())

cost=[[] for i in range(n+1)]

for i in range(m):
    s,e,c=map(int,input().split())
    cost[s].append((e,c))

start,end=map(int,input().split())

dist=[float('inf')]*(n+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0

    while q:
        d,curr=heapq.heappop(q)

        # 이미 처리된 적 있는 노드라면 무시
        if dist[curr]<d:
            continue

        for neighbor, weight in cost[curr]:
            new_cost=d+weight
            # 현재 노드를 거쳐서 가는 게 더 빠르면 갱신
            if new_cost<dist[neighbor]:
                dist[neighbor]=new_cost
                heapq.heappush(q,(new_cost,neighbor))

dijkstra(start)

print(dist[end])