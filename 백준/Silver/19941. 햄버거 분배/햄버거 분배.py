import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

x = list(input().rstrip())
ans = 0

for i in range(n):
    if x[i] == "P":
        for idx in range(max(0, i - k), min(n, i + k + 1)):
            if x[idx] == "H":
                x[idx] = "X"
                ans += 1
                break

print(ans)
