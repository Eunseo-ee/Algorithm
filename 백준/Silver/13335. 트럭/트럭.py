import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
n, w, l = map(int, input().split())  # n = 트럭 수, w = 다리 길이, l = 다리 최대 하중
a = deque(map(int, input().split()))  # 트럭의 무게 리스트를 덱으로 변환

# 다리를 건너는 트럭을 관리할 deque (무게, 경과 시간)
bridge = deque()
time = 0  # 총 걸린 시간
current_weight = 0  # 현재 다리 위 트럭들의 총 무게

while a or bridge:
    time += 1  # 시간 증가

    # 다리를 빠져나가는 트럭 처리
    if bridge and bridge[0][1] == w:  # 가장 앞의 트럭이 도착했으면 제거
        truck_weight, _ = bridge.popleft()
        current_weight -= truck_weight

    # 새로운 트럭 추가 가능하면 추가
    if a and current_weight + a[0] <= l:  # 새로운 트럭을 추가할 수 있는 경우
        truck_weight = a.popleft()
        bridge.append((truck_weight, 0))  # (무게, 다리에서 경과한 시간)
        current_weight += truck_weight

    # 다리 위의 모든 트럭의 경과 시간 증가
    for i in range(len(bridge)):
        bridge[i] = (bridge[i][0], bridge[i][1] + 1)

print(time)
