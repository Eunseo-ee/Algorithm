import sys
from collections import deque
input=sys.stdin.readline

k=int(input())
tree=list(map(int,input().split()))
keep = [[] for _ in range(k)]

def div(arr,depth):
    if not arr:
        return

    mid = len(arr) // 2  # 가운데 값 선택
    keep[depth].append(arr[mid])  # 해당 깊이에 추가

    div(arr[:mid], depth + 1)  # 왼쪽 서브트리
    div(arr[mid + 1:], depth + 1)  # 오른쪽 서브트리

div(tree, 0)

for level in keep:
    print(*level)