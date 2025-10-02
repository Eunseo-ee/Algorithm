def solution(s):
    answer = 0
    
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        tmp = ''
        prev = s[0:step]
        cnt = 1
        ans = ''
        for j in range(step, len(s), step):
            tmp = s[j:j+step] 
            if tmp == prev:
                cnt += 1
            else:
                if cnt >= 2:
                    ans += str(cnt)+prev
                    cnt = 1
                    prev = tmp
                    tmp = ''
                else:
                    ans += prev
                    prev = tmp
                    tmp = ''
        if cnt>=2:
            ans+=str(cnt)+prev
        else:
            ans+=prev
            
        answer = min(len(ans), answer)
        
    return answer