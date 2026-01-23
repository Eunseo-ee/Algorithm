import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

# 1. 예외 처리: 모든 방문자 수가 0인 경우
if max(visit) == 0:
    print("SAD")
    sys.exit()

# 2. 첫 번째 윈도우 초기화
curr_sum = sum(visit[0:x])
ans = curr_sum
cnt = 1

# 3. 슬라이딩 윈도우 진행 (1부터 n-x까지)
for i in range(1, n - x + 1):
    # i번째에서 끝나는 윈도우의 합 = 이전 합 - 나간 놈(i-1) + 들어온 놈(i+x-1)
    curr_sum = curr_sum - visit[i - 1] + visit[i + x - 1]
    
    if curr_sum > ans:
        ans = curr_sum
        cnt = 1  # 새로운 최댓값이 나오면 개수 초기화
    elif curr_sum == ans:
        cnt += 1 # 기존 최댓값과 같으면 개수 추가

print(ans)
print(cnt)