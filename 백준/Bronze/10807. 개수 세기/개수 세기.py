n=int(input())
num=list(map(int,input().split()))
k=int(input())
cnt=0

for i in num:
    if i==k:cnt+=1
        
print(cnt)