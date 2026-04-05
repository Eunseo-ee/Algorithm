import os
import urllib.parse
import requests  # 티어 조회를 위해 필요 (pip install requests)
import time

# 1. 설정
root_dir = "백준"
target_dirs = ["Gold"]
user_id = "secondtooth"  # 여기에 본인 백준 ID를 넣으세요


# solved.ac 티어 숫자 -> 아이콘 번호 매칭
# 1~5: Bronze, 6~10: Silver, 11~15: Gold ...
def get_tier_icon(problem_id):
    try:
        # solved.ac API 호출 (문제 상세 정보)
        url = f"https://solved.ac/api/v3/problem/show?problemId={problem_id}"
        response = requests.get(url)
        if response.status_code == 200:
            tier = response.json().get('level', 0)
            return f'<img src="https://static.solved.ac/tier_small/{tier}.svg" width="20">'
    except:
        pass
    return '<img src="https://static.solved.ac/tier_small/0.svg" width="20">'  # 못 찾으면 0(Unrated)


# 수정 제안: 카드와 스트릭 사이의 간격을 조절한 헤더
base_readme_header = f"""# 🏆 Algorithm Study (Gold Focus)

<p align="center">
  <a href="https://solved.ac/profile/{user_id}">
    <img src="https://mazassumnida.wtf/api/v2/generate_badge?boj={user_id}" alt="Solved.ac 프로필">
  </a>

</p>


> **서울과학기술대학교 컴퓨터공학과 4학년**
> 실시간 티어 데이터를 연동하여 관리하는 골드 문제 오답 노트입니다. 🔥

---

## 📊 Gold 문제 풀이 현황
| 난이도 | 번호 | 문제 제목 | 풀이 코드 | 핵심 정리 |
| :---: | :---: | :--- | :---: | :---: |
"""

rows = []

if os.path.exists(root_dir):
    for target in target_dirs:
        target_path = os.path.join(root_dir, target)
        if not os.path.exists(target_path): continue

        problem_folders = [f for f in os.listdir(target_path) if os.path.isdir(os.path.join(target_path, f))]

        try:
            problem_folders.sort(key=lambda x: int(x.split('.')[0]))
        except:
            problem_folders.sort()

        for folder in problem_folders:
            if "." not in folder: continue

            num = folder.split(".", 1)[0].strip()
            title = folder.split(".", 1)[1].strip()

            print(f"🔄 {num}번 문제 티어 정보 가져오는 중...")
            tier_icon = get_tier_icon(num)
            time.sleep(0.1)  # API 과부하 방지용 짧은 휴식

            # URL 인코딩
            encoded_root = urllib.parse.quote(root_dir)
            encoded_target = urllib.parse.quote(target)
            encoded_folder = urllib.parse.quote(folder)

            # .py 파일 탐색
            inner_path = os.path.join(target_path, folder)
            files = os.listdir(inner_path)
            py_file = next((f for f in files if f.endswith(".py")), "")
            encoded_py = urllib.parse.quote(py_file)

            code_link = f"[Python](./{encoded_root}/{encoded_target}/{encoded_folder}/{encoded_py})"
            note_link = f"[Note](./{encoded_root}/{encoded_target}/{encoded_folder}/README.md)"
            boj_link = f"[{title}](https://www.acmicpc.net/problem/{num})"

            rows.append(f"| {tier_icon} | {num} | {boj_link} | {code_link} | {note_link} |")

# 파일 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(base_readme_header)
    f.write("\n".join(rows))
    f.write(f"\n\n--- \n*마지막 업데이트: 2026-04-04*")

print(f"✅ 티어 연동 완료! 총 {len(rows)}개의 문제를 정리했습니다.")