# 사용 방법

<h1>설치 | Installation</h1>
```
$ git clone https://github.com/jjweidon/musinsa-review-crawler.git
$ cd musinsa-review-crawler
# pip 가상환경 실행
$ pipenv shell
$ pip install -r ./requirements.txt
```

<h1>설정 | Setting</h1>
<h3>csv 파일을 생성할 경로 설정</h3>
```
FILE_PATH = 'C:/Users/weidon/Desktop/myproject/musinsa-review-crawler/sample.csv'
```
<h3>파일 모드 선택. 처음 파일 생성할 때는 w, 이후 행만 추가할 때는 a</h3>
```
MODE = 'w'
```
<h3>시작 상품코드, 끝 상품코드 설정</h3>
```
START = 3001200
END = 3002000
```

<h1>실행 | Usage</h1>
```
$ python main.py
```