# 사용 방법

<h2>설치 | Installation</h2>
git clone https://github.com/jjweidon/musinsa-review-crawler.git
cd musinsa-review-crawler

<h3>pip 가상환경 실행</h3>
pipenv shell
pip install -r ./requirements.txt

<h2>설정 | Setting</h2>
<h3>카테고리 코드 설정</h3>
CATEGORY_CODE = "001"
<h3>csv 파일을 생성할 경로 설정</h3>
FILE_PATH = 'C:/Users/weidon/Desktop/myproject/musinsa-review-crawler/{CATEGORY_CODE}.csv'
<h3>파일 모드 선택. 처음 파일 생성할 때는 w, 이후 행만 추가할 때는 a</h3>
MODE = 'w'
<h3>시작 페이지 번호, 끝 페이지 번호 설정</h3>
START = 1
END = 2
앞 번호에는 후기가 많으니 조금씩 나누는 것 추천

<h2>실행 | Usage</h2>
python main.py