def solution(id_list, report, k):
    answer = []
    check={}
    for i in report:
        tmp=i.split()
        if tmp[1] not in check:
            check[tmp[1]]=[]
        if tmp[0] not in check[tmp[1]]:
            check[tmp[1]].append(tmp[0])
            
    answer=[0 for i in range(len(id_list))]
    chk=[0 for i in range(len(id_list))]
    
    for i in range (len(id_list)):
        if id_list[i] in check:
            chk[i]=len(check[id_list[i]])
        else:
            chk[i]=0
            
    for i in range(len(id_list)):
        if chk[i] >= k:   # i번째 유저가 정지 대상이라면
            banned_user = id_list[i]
            for reporter in check[banned_user]:   # 이 유저를 신고한 사람들
                answer[id_list.index(reporter)] += 1
    return answer