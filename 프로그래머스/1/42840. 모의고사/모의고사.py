def solution(answers):
    answer = []
    
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    score=[0,0,0,0]
    
    for i in range(len(answers)):
        if answers[i]==one[i%len(one)]:score[1]+=1
        if answers[i]==two[i%len(two)]:score[2]+=1
        if answers[i]==three[i%len(three)]:score[3]+=1
    
    M=max(score)
    
    for i in range(4):
        if score[i]==M:
            answer.append(i)
            
    return answer