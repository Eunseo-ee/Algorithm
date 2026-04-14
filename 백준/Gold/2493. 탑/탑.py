import sys
input = sys.stdin.readline
from collections import deque
import heapq

import sys
input = sys.stdin.readline

n=int(input())
tower=list(map(int, input().split()))

stack = [] # (높이, 번호)를 담을 스택
ans = []   # 수신 결과를 담을 리스트

for i in range(n):
    current_height=tower[i]
    current_num = i+1 # 탑 번호는 1번부터 시작

    while stack:
        # 스택의 맨 위 탑이 현재 나보다 높은지 확인
        if stack[-1][0] >= current_height:
            ans.append(stack[-1][1]) # 수신 탑 번호 기록
            break
        else:
            stack.pop() # 나보다 낮은 탑은 제거 (다시 쓰일 일 없음)

    if not stack: # 스택이 비었따면 수신할 탑이 없는 것
        ans.append(0)

    # 현재 탑을 스택에 추가 (다음 탑들을 위해)
    stack.append((current_height, current_num))

print(*(ans))