import queue
import sys
from collections import deque

input=sys.stdin.readline

##############################################################################################

N = int(input())
arr = list(map(int, input().split()))

# 1) 중복 제거 후 정렬
uniq = sorted(set(arr))  # 오름차순

# 2) 값 -> 압축값(랭크) 맵핑
rank = {v: i for i, v in enumerate(uniq)}

# 3) 원본 순서대로 출력
out = [str(rank[x]) for x in arr]
print(' '.join(out))
