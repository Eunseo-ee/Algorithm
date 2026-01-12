import sys
input = sys.stdin.readline

index=0

while True:
    index+=1
    ans=0

    n=int(input())

    if n==0:
        break

    cost=[]

    for i in range(n):
        cost.append(list(map(int,input().split())))

    cost[0][0]=float('inf')
    cost[0][2]+=cost[0][1]

    ans+=cost[0][1]
    last=1

    for i in range(1,n):
        #0번 칸
        cost[i][0]+=min(cost[i-1][0],cost[i-1][1])
        #1번 칸
        cost[i][1]+=min(cost[i-1][0], cost[i-1][1], cost[i-1][2], cost[i][0])
        #2번 칸
        cost[i][2] += min(cost[i-1][1], cost[i-1][2], cost[i][1])

    print(f"{index}. {cost[n-1][1]}")