import queue
import sys
from collections import deque

# R : 수의 순서 뒤집기
# D : 첫번째 수 버리기 (비어있는데 사용하면 에러 발생)

t=int(input())

for _ in range(t):
    p=input()
    n=int(input())
    tmp=input()
    tmp=tmp[1:-1]
    flag=True

    if n==0:
        num=deque()
    else:
        num = deque(map(int, tmp.split(',')))

    reverse_cnt=0

    for i in range(len(p)):
        if p[i]=='R':
            reverse_cnt+=1

        else: # p[i]=='D'
            if len(num)==0:
                flag=False
                print("error")
                break
            else:
                if reverse_cnt%2==0:
                    num.popleft()
                else:
                    num.pop()

    if flag:
        if reverse_cnt % 2 == 1:
            num.reverse()
        print('[' + ','.join(map(str, num)) + ']')