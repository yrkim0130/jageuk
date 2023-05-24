import requests
import json
import random
# 추가 템플릿을 로드하기 위해 함수를 추가했다.
from flask import Flask, render_template

# 영어 조언 API 불러오기
def get_eng_advice():
    # {"slip": { "id": 74, "advice": "asdasdasd."}}
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()
    eng = data['slip']['advice'] # 영어 명언
    return eng

# 한글 조언 파일 불러오기
json_file_path = "hangeul.json"
def get_kor_advice():
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        # 랜덤으로 조언 선택
        adv = random.choice(data["jageuk"])
        kor = adv['advice'] # 한글 명언
        aut = adv['author'] # 작가
        return kor, aut

# 플라스크 객체를 생성하며 웹 템플릿 디렉토리 설정
app = Flask(__name__, static_folder="templates/static")

# 한글 명언 페이지(메인)
@app.route('/')
def jageuk():
    kor, aut = get_kor_advice()  # 한글 명언
    kor = f"{kor} - {aut} -"  # 한글 명언과 작가를 결합
    return render_template('index.html', kor=kor)
    
# 영어 명언 페이지
@app.route('/eng')
def jageuk_eng():
    eng = get_eng_advice()
    return render_template('index.html', eng=eng)

# 웹 애플리케이션 실행
if __name__ == '__main__':
    app.run()