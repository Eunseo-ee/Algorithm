def solution(friends, gifts):
    answer = 0
    
    # ans[준사람][받은사람]
    ans=[[0 for i in range(len(friends))] for j in range(len(friends))]
    num=[]
    gift=[0 for i in range(len(friends))]
    
    for i in gifts:
        a,b=i.split() # a= 준 사람, b= 받은 사람
        ans[friends.index(a)][friends.index(b)]+=1
    
    for i in range(len(friends)):
        tmp=0
        for j in range(len(friends)):
            tmp+=ans[j][i]
        num.append(sum(ans[i])-tmp)
        
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            # 선물 준 개수 차이나는 경우
            if ans[i][j]!=ans[j][i]:
                if ans[i][j]>ans[j][i]:
                    gift[i]+=1
                else:
                    gift[j]+=1
            else:
                if num[i]==num[j]:
                    continue
                else:
                    if num[i]>num[j]:
                        gift[i]+=1
                    else:
                        gift[j]+=1
                        
    answer=max(gift)
    
    return answer

# 저번달에 선물 덜 준 사람이 선물 줌
# 똑같거나 기록 없으면 (이번달까지 자기가 준 선물 수)-(받은 선물 수) 값이 작은 사람이 선물 줌
# 선물지수도 똑같으면 선물 안 주고받음
# => 선물 가장 많이 받을 친구는 몇개 받을지?

# gifts= [준사람 받은사람]
