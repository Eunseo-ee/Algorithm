import queue
import sys
from collections import deque

input = sys.stdin.readline

while True:
    a,b,c=input().split()
    if a=='#' and b=='0' and c=='0':
        exit(0)
    if int(b)>17 or int(c)>=80:
        print(a, "Senior")
    else:
        print(a, "Junior")
