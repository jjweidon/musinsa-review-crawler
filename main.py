import csv

from time import sleep
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from typing import Dict,List

FILE_PATH = 'C:/Users/weidon/Desktop/myproject/musinsa-review-crawler/sample.csv' # csv 파일 설치 경로
MODE = 'a' # 새 파일 생성: w, 행만 추가: a
START = 3001200 # 시작 상품 코드
END = 3001300 # 끝 상품 코드

with open(FILE_PATH, MODE, encoding='utf-8-sig', newline='') as f:
    fieldnames = ['상품코드', '브랜드명', '상품명', '가격', '성별', '리뷰내용', '옵션', '키', '몸무게', '배송', '포장', '사이즈', '밝기', '색감', '두께감', '보온성', '무게감', '발색력', '지속력', '수분감', '수납공간']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    options = webdriver.ChromeOptions()
    # options.add_argument("headless") # 크롬 창 안띄우기
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)

    for code in range(START, END+1):
        url = f"https://www.musinsa.com/app/goods/{code}"

        try:
            driver.get(url)
            sleep(1)

            # 웹 페이지 호출 상태 점검
            if driver.page_source:
                print(f"{code} 웹 페이지 가져오기 성공!")
            else:
                print(f"{code} 웹 페이지 가져오기 실패!")
                continue

            # html 요소 찾기
            soup = bs(driver.page_source, 'lxml')

            # 상품 변수 초기화
            brand = "-"
            name = "-"
            price = 0

            # 상품명 찾기
            product_title = soup.find("span", attrs={"class": "product_title"})
            name = product_title.find("em").text.strip()

            # 브랜드명 찾기
            product_info = soup.find("div", attrs={"class": "product_info_section"})
            product_article_contents = product_info.find("p", attrs={"class": "product_article_contents"})
            brand = product_article_contents.find("a").text.strip()
            
            # 가격 찾기
            price_info = soup.find("div", attrs={"class": "price_info_section"})
            price = price_info.find("span", attrs={"id": "goods_price"}).text.split("원")[0].strip()

            print(f"상품코드: {code}, 상품명: {name}, 브랜드명: {brand}, 가격: {price}원")

            # 후기 타입들 가져오기 (체험단 후기, 스타일 후기, 상품 후기, 일반 후기)
            estimateBox = soup.find("div", attrs={"id": "estimateBox"})
            estimates_ul = estimateBox.find("ul", attrs={"class": "snb"})
            if not estimates_ul:
                continue
            estimates = estimates_ul.find_all("li", attrs={"class": "btnReviewTypeTab"})
            for i, estimate in enumerate(estimates):
                # 후기 타입 클릭
                element = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[@id="estimateBox"]/div[2]/ul/li[{i+1}]'))
                )
                element.click()
                sleep(0.5)
                review_type = estimate.text.split(' (')[0].lstrip()
                print(f"{code}: {review_type} 클릭")

                # 리뷰 목록 가져오기
                soup = bs(driver.page_source, 'lxml')
                review_wrap = soup.find("div", attrs={"class": "review-list-wrap"})

                # 리뷰 없으면 그대로 진행
                if review_wrap.find("div", attrs={"class": "review-list--none"}):
                    print("후기 없음")
                    continue

                # 페이지 수 가져오기
                box_page_msg = review_wrap.find("div", attrs={"class": "box_page_msg"}).text.strip().split(' 페이지')[0]
                pages = int(box_page_msg)
                print(f"총 {pages}페이지 탐색")

                for p in range(pages):
                    # print(f"{code} {review_type}의 {p+1}/{pages} 페이지 보는 중")

                    # 리뷰 목록 가져오기
                    soup = bs(driver.page_source, 'lxml')
                    review_wrap = soup.find("div", attrs={"class": "review-list-wrap"})

                    # 리뷰 개수 구하기
                    review_list = review_wrap.find_all("div", attrs={"class": "review-list"})
                    review_cnt = len(review_list)
                    # 리뷰 목록
                    for r, review in enumerate(review_list):
                        # 변수 초기화
                        sex = "-"
                        height = 0
                        weight = 0
                        content = "-"
                        option = "-"
                        star = 0
                        delivary = "-"
                        packaging = "-"
                        size = "-"
                        brightness = "-"
                        color = "-"
                        thickness = "-"
                        warmth = "-"
                        weightness = "-"
                        pigmented = "-"
                        consistency = "-"
                        moisture = "-"
                        storage = "-"

                        # 성별, 키, 몸무게
                        review_profile = review.find("div", attrs={"class": "review-profile"})
                        profile_body = review_profile.find("p", attrs={"class": "review-profile__body_information"})
                        if profile_body:
                            profile_datum = profile_body.get_text().split(" · ")
                            for p_data in profile_datum:
                                if "성" in p_data:
                                    sex = p_data.split("성")[0]
                                if "cm" in p_data:
                                    height = int(p_data.split("cm")[0])
                                if "kg" in p_data:
                                    weight = int(p_data.split("kg")[0])

                        # 리뷰 내용
                        review_contents_body = review.find("div", attrs={"class": "review-contents"})
                        review_contents = review_contents_body.find("div", attrs={"class": "review-contents__text"})
                        if review_contents:
                            content = review_contents.text.strip()

                        # 상세 평가
                        review_evaluations = review_contents_body.find_all("li", attrs={"class": "review-evaluation--type3__item"})
                        for evaluation in review_evaluations:
                            evalutate_type, evaluate_detail = evaluation.text.split()[0], evaluation.text.split()[-1]
                            if evalutate_type == "배송":
                                delivary = evaluate_detail
                            elif evalutate_type == "포장":
                                packaging = evaluate_detail
                            elif evalutate_type == "사이즈":
                                size = evaluate_detail
                            elif evalutate_type == "밝기":
                                brightness = evaluate_detail
                            elif evalutate_type == "색감":
                                color = evaluate_detail
                            elif evalutate_type == "두께감":
                                thickness = evaluate_detail
                            elif evalutate_type == "보온성":
                                warmth = evaluate_detail
                            elif evalutate_type == "무게감":
                                weightness = evaluate_detail
                            elif evalutate_type == "발색력":
                                pigmented = evaluate_detail
                            elif evalutate_type == "지속력":
                                consistency = evaluate_detail
                            elif evalutate_type == "수분감":
                                moisture = evaluate_detail
                            elif evalutate_type == "수납공간":
                                storage = evaluate_detail

                        # 옵션
                        goods_information = review.find("div", attrs={"class": "review-goods-information__item"})
                        if goods_information:
                            option = goods_information.find("span", attrs={"class": "review-goods-information__option"}).text.strip()
                        
                        print(f"{code} {review_type}의 {p+1}/{pages} 페이지에서 {r+1}번째 리뷰")
                        writer.writerow({'상품코드': code, '브랜드명': brand, '상품명': name, '가격': price,
                                        '성별': sex, '리뷰내용': content, '옵션': option, '키': height, '몸무게': weight,
                                        '배송': delivary, '포장': packaging, '사이즈': size, '밝기': brightness, '색감': color,
                                        '두께감': thickness, '보온성': warmth, '무게감': weightness, '발색력': pigmented, '지속력': consistency, '수분감': moisture, '수납공간': storage})

                    # 다음 페이지 번호 클릭
                    if p+1 == pages:
                        break
                    page_number = (p % 5) + 4
                    element = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH, f'//*[@id="reviewListFragment"]/div[{review_cnt+1}]/div[2]/div/a[{page_number}]'))
                    )
                    element.click()
                    sleep(0.5)
                    
        except WebDriverException:
            print(f"{code}는 없는 상품 페이지")
            continue

f.close()