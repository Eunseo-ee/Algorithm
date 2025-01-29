import sys
from collections import deque

input = sys.stdin.readline

def find_year(m,n,x,y):
    while x<=m*n:
        if (x-1)%n+1==y:
            return x
        x+=m
    return -1

for _ in range(int(input())):
    m,n,x,y=map(int,input().split())

    print(find_year(m,n,x,y))