import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())

if n%2==0:
    print("CY")
else:
    print("SK")