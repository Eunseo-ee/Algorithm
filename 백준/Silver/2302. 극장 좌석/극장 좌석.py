import sys
from collections import deque
import heapq

input = sys.stdin.readline

# 피보나치 수열 (좌석 자리 바꾸는 경우의 수)
def fibonacci(n):
    fib = [1] * (n + 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

n=int(input())
seat=[0 for i in range(n+1)]
m=int(input()) # 고정석 개수
for _ in range(m):
    seat[int(input())]=1

cnt=0
ans=1

if n==m:
    print(1)
    exit(0)

fib = fibonacci(n)

for i in range(1,n+1):
    if seat[i]==0:
        cnt+=1
    elif seat[i]==1 and cnt!=0:
        ans*=fib[cnt]

        cnt=0
    if i==n:
        ans*=fib[cnt]

print(ans)