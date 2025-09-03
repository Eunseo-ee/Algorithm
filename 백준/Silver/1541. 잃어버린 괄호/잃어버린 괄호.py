import sys
input=sys.stdin.readline

eql=input().split('-')
num=[]

for i in eql:
    SUM=0
    tmp=i.split('+')
    for j in tmp:
        SUM += int(j)
    num.append(SUM)
    
n=num[0]

for i in range(1,len(num)):
    n-=num[i]
print(n)