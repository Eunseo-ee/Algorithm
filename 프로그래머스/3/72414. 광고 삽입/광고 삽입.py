def time_to_sec(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

def sec_to_time(s):
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    
    # [0, play_sec] 범위용 배열
    total = [0] * (play_sec + 2)
    
    # 로그 기록 반영 (차분 배열)
    for log in logs:
        start, end = log.split("-")
        s = time_to_sec(start)
        e = time_to_sec(end)
        total[s] += 1
        total[e] -= 1
    
    # 1차 누적합: 각 초 시청자 수
    for i in range(1, play_sec + 1):
        total[i] += total[i - 1]
    
    # 2차 누적합: 0초~i초까지 누적 시청시간
    for i in range(1, play_sec + 1):
        total[i] += total[i - 1]
    
    # 광고 구간 최대 누적 시청시간 탐색
    max_watch = total[adv_sec - 1]   # 0~adv_sec-1까지
    best_start = 0
    
    for start in range(1, play_sec - adv_sec + 1):
        end = start + adv_sec - 1
        watch = total[end] - total[start - 1]
        if watch > max_watch:
            max_watch = watch
            best_start = start
    
    return sec_to_time(best_start)
