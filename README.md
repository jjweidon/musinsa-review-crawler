# 사용 방법

<h2>설치 | Installation</h2>
git clone https://github.com/jjweidon/musinsa-review-crawler.git
cd musinsa-review-crawler

<h5>pip 가상환경 실행</h5>
pipenv shell
pip install -r ./requirements.txt

<h2>설정 | Setting</h2>
<h5>csv 파일을 생성할 경로 설정</h5>
FILE_PATH = 'C:/Users/weidon/Desktop/myproject/musinsa-review-crawler/sample.csv'
<h5>파일 모드 선택. 처음 파일 생성할 때는 w, 이후 행만 추가할 때는 a</h5>
MODE = 'w'
<h5>시작 상품코드, 끝 상품코드 설정</h5>
START = 3001200
END = 3002000

<h2>실행 | Usage</h2>
python main.py