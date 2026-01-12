import sys
input = sys.stdin.readline

n = int(input())
MOD = 1000000000

# 1. 부호 판단 및 출력
if n > 0:
    print(1)
elif n < 0:
    # 음수 영역: 홀수번째는 양수, 짝수번째는 음수
    if abs(n) % 2 == 0:
        print(-1)
    else:
        print(1)
else:
    print(0)

# 2. 피보나치 값 계산 (절대값 n 기준)
target = abs(n)
if target == 0:
    print(0)
elif target == 1:
    print(1)
else:
    # 메모리를 아끼기 위해 n만큼만 배열 생성
    dp = [0] * (target + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, target + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[target])