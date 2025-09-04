import sys

input = sys.stdin.readline

def solve(idx, SUM):
    global ans
    # 종료 조건: 모든 원소를 탐색한 경우
    if idx == N:
        return

    # 현재 원소를 부분수열에 포함
    if SUM + nums[idx] == S:  # 합이 S가 되는 경우 카운트
        ans += 1

    # 재귀 호출
    solve(idx + 1, SUM + nums[idx])  # 현재 원소를 포함한 상태
    solve(idx + 1, SUM)  # 현재 원소를 포함하지 않는 상태

# 입력 받기
N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

# 재귀 호출 시작
solve(0, 0)
print(ans)
