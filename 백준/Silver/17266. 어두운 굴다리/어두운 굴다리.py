import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())

light = list(map(int, input().split()))
max_interval = 0

ans = max(light[0], n - light[m - 1])

for i in range(1, m):
    max_interval = max(max_interval, light[i] - light[i - 1])

ans = max(ans, (max_interval + 1) // 2)
print(ans)
