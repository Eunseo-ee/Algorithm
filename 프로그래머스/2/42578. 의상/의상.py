def solution(clothes):
    answer = 1
    closet={}
    
    for x,y in clothes:
        closet[y]=closet.get(y, 0)+1
        
    for i in closet.values():
        answer*=(i+1)
    
    return answer-1