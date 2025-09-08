import queue
import sys
from collections import deque

input=sys.stdin.readline

###################################################################

na, nb=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))

print(len(a-b))
print(*sorted(list(a-b)))