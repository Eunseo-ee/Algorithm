import math
from itertools import permutations

def odd(n):
    M=10**n
    
    chk=[True]*(M+1)
    res=[]
    chk[0], chk[1]=False, False
    
    for i in range(2,int(math.sqrt(M))+1):
        if chk[i]:
            res.append(i)
            j=2
            while i*j<=M:
                chk[i*j]=False
                j+=1
    res = [x for x in range(M+1) if chk[x]]
    return res
    

def solution(numbers):
    answer = 0
    per_num = set()
    
    odds=odd(len(numbers))
    
    num=[]
    
    for i in range(len(numbers)):
        num.append(numbers[i])
        
    for i in range(1,len(num)+1):
        temp = list(permutations(numbers, i))
        per_num.update(int(''.join(j)) for j in temp)
        
    for i in per_num:
        if i in odds:
            answer+=1
    
    return answer