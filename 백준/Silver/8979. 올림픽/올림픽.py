import sys
input = sys.stdin.readline
import heapq

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
countries = []

for _ in range(n):
    # 국가 번호까지 같이 저장해야 나중에 K를 찾을 수 있습니다.
    data = list(map(int, input().split()))
    countries.append(data)
    if data[0] == k:
        target = data # 우리가 찾는 K국가의 정보

# 1. 금, 은, 동 순서로 내림차순 정렬
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 2. 등수 계산: 나보다 잘한 나라가 몇 개인지 센다
rank = 1
for c in countries:
    # 금, 은, 동 점수를 비교 (국가 번호인 x[0]은 제외)
    if (c[1], c[2], c[3]) > (target[1], target[2], target[3]):
        rank += 1

print(rank)