import sys
input = sys.stdin.readline

n = int(input())
channel = []
for _ in range(n):
    channel.append(input().strip())

# 1. KBS1 이동
idx1 = channel.index('KBS1')
for _ in range(idx1): print(1, end='') # 커서 내리기
for _ in range(idx1): print(4, end='') # 채널 올리기

# KBS1을 앞으로 보냈으므로 리스트를 실제로 갱신하거나, 
# KBS2의 인덱스를 다시 찾아야 합니다.
target = channel.pop(idx1)
channel.insert(0, target)

# 2. KBS2 이동
idx2 = channel.index('KBS2')
for _ in range(idx2): print(1, end='') # 커서 내리기
for _ in range(idx2 - 1): print(4, end='') # 채널 올리기 (1번 인덱스까지만!)