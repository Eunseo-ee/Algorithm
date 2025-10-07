from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    db = defaultdict(list)
    
    # 1️⃣ info 전처리
    for i in info:
        data = i.split()
        conditions = data[:-1]  # ['java', 'backend', 'junior', 'pizza']
        score = int(data[-1])
        
        # 가능한 모든 조합 (0~4개 -)
        for n in range(5):
            for comb in combinations(range(4), n):
                temp = conditions.copy()
                for c in comb:
                    temp[c] = '-'
                key = ''.join(temp)
                db[key].append(score)
    
    # 2️⃣ 각 조건별 점수 정렬
    for value in db.values():
        value.sort()
    
    # 3️⃣ query 처리
    answer = []
    for q in query:
        q = q.replace(' and ', ' ')
        q = q.split()
        key = ''.join(q[:-1])
        target = int(q[-1])
        
        if key in db:
            scores = db[key]
            # 이진 탐색 (target 이상 점수의 개수)
            idx = bisect.bisect_left(scores, target)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    
    return answer