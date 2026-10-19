from collections import Counter

def solution(participant, completion):
    # 두 카운터의 차집합 계산
    result = Counter(participant) - Counter(completion)
    # 남은 단 하나의 키 반환
    return list(result.keys())[0]