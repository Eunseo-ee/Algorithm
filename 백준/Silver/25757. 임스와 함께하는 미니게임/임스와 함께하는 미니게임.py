import sys
input = sys.stdin.readline
import heapq

import sys
input = sys.stdin.readline

n,g=input().split()
friend=[]
# 2,3,4

for i in range(int(n)):
    friend.append(input())

friend=list(set(friend))

if g=='Y':
    print(len(friend))

if g=='F':
    print(len(friend)//2)

if g=='O':
    print(len(friend)//3)