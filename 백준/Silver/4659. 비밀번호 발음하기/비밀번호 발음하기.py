import sys
input = sys.stdin.readline
import heapq

import sys
input = sys.stdin.readline

while True:
    x=input().rstrip()
    if x=="end":
        break
    
    accept=True
    
    if not any(vowel in x for vowel in 'aeiou'):
        accept=False
        print(f'<{x}> is not acceptable.')
        continue

    vowels = "aeiou"
    v_cnt = 0  # 연속 모음 개수
    c_cnt = 0  # 연속 자음 개수

    for char in x:
        if char in vowels:
            v_cnt += 1
            c_cnt = 0  # 자음 연속성 끊김
        else:
            c_cnt += 1
            v_cnt = 0  # 모음 연속성 끊김

        # 중간에 하나라도 3이 되면 실패!
        if v_cnt == 3 or c_cnt == 3:
            accept=False
            print(f'<{x}> is not acceptable.')
            continue
    
    for i in range(len(x)-1):
        if x[i]==x[i+1] and x[i]!='e' and x[i]!='o':
            accept=False
            print(f'<{x}> is not acceptable.')
            continue

    if accept:
        print(f'<{x}> is acceptable.')