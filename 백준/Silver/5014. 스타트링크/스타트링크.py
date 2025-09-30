from collections import deque

def elevator(F, S, G, U, D):
    # 방문 배열
    visited = [False] * (F + 1)
    
    # BFS 큐: (현재 층, 버튼 누른 횟수)
    queue = deque([(S, 0)])
    visited[S] = True  # 시작 층 방문 처리
    
    while queue:
        current_floor, steps = queue.popleft()
        
        # 목표 층에 도달한 경우
        if current_floor == G:
            return steps
        
        # 위로 이동
        if current_floor + U <= F and not visited[current_floor + U]:
            visited[current_floor + U] = True
            queue.append((current_floor + U, steps + 1))
        
        # 아래로 이동
        if current_floor - D >= 1 and not visited[current_floor - D]:
            visited[current_floor - D] = True
            queue.append((current_floor - D, steps + 1))
    
    # BFS 종료 후에도 G층에 도달하지 못한 경우
    return "use the stairs"

# 입력 처리
F, S, G, U, D = map(int, input().split())
print(elevator(F, S, G, U, D))
