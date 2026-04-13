import sys
input = sys.stdin.readline
from collections import deque
import heapq

import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

# 찾기 연산 (같은 집합에 속하는지 확인하기 위한 함수)
def find_parent(x):
    if parent[x] != x:
        parent[x]=find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    
    if a<b : # 값이 더 작은 쪽을 부모로
        parent[b]=a
    else:
        parent[a]=b

for i in range(m):
    op, a, b= map(int, input().split())

    if op == 0:
        union_parent(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")