import sys
input = sys.stdin.readline
import heapq

h,w,n,m=map(int,input().split())
n+=1
m+=1

col=h//n
row=w//m

if w%m!=0:
    row+=1

if h%n!=0:
    col+=1


print(row*col)