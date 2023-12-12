import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

# 무신사 폰트 경로 설정 (시스템에 설치된 폰트 경로에 따라 수정 필요)
font_path = "C:/Users/weidon/AppData/Local/Microsoft/Windows/Fonts/musinsa-Medium.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일 불러오기
data = pd.read_csv('./data/data.csv')

data1 = data.copy()

data1.describe()

print(data['키'].isnull().any())
print(data['몸무게'].isnull().any())
print(data['옵션'].isnull().any())
data = data.dropna()

data1 = data1.query("키 != '-' and 몸무게 != '-' and 옵션 != '-'")

print(data['키'].isnull().sum())  # '키' 열의 NaN 값 개수 출력
print(data['몸무게'].isnull().sum())  # '몸무게' 열의 NaN 값 개수 출력
print(data['옵션'].isnull().sum())  # '옵션' 열의 NaN 값 개수 출력

print(len(data['키']))  # '키' 열의 길이 출력
print(len(data['몸무게']))  # '몸무게' 열의 길이 출력
print(len(data['옵션']))  # '옵션' 열의 길이 출력

# '옵션' 열에서 S, M, L, XL, XXL 값을 숫자로 매핑
size_mapping = {'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
data1['옵션'] = data1['옵션'].map(size_mapping)

# '키'와 '몸무게' 열을 숫자형으로 변환
data1['키'] = pd.to_numeric(data1['키'], errors='coerce')
data1['몸무게'] = pd.to_numeric(data1['몸무게'], errors='coerce')

plt.figure(1)
# 산점도 그리기
plt.scatter(data1['키'], data1['몸무게'], c=data1['옵션'], cmap='viridis')

# 컬러바 추가
plt.colorbar(label='옵션')

# x축과 y축의 범위 지정
plt.xlim(120, 200)
plt.ylim(0, 120)

# 라벨과 제목 추가
plt.xlabel('height')
plt.ylabel('weight')
plt.title('키와 몸무게에 따른 옵션 분포')

# 그래프 보여주기
plt.show()

data = pd.read_csv('./data/data.csv')

print(data['가격'].isnull().sum())  # '가격' 열의 NaN 값 개수 출력
print(data['색감'].isnull().sum())  # '색감' 열의 NaN 값 개수 출력

print(len(data['가격']))  # '가격' 열의 길이 출력
print(len(data['색감']))  # '색감' 열의 길이 출력

# '색감'이 '보통이에요', '선명해요', '흐려요'인 데이터만 추출
filtered_data = data[data['색감'].isin(['보통이에요', '선명해요', '흐려요'])]

# '색감'에 대한 평균 '가격' 계산
filtered_data['가격'] = pd.to_numeric(filtered_data['가격'], errors='coerce')
mean_price_by_color = filtered_data.groupby('색감')['가격'].mean()

# 막대 그래프 그리기
plt.figure(2)
plt.bar(mean_price_by_color.index, mean_price_by_color, color='skyblue')
plt.xlabel('color')  # x축 라벨
plt.ylabel('average price')  # y축 라벨
plt.title('색감에 따른 평균 가격')  # 제목
plt.show()

filtered_data = data[data['두께감'].isin(['보통이에요', '두꺼워요', '얇아요'])]
# '색감'에 대한 평균 '가격' 계산
data['가격'] = pd.to_numeric(data['가격'], errors='coerce')
mean_price_by_color = filtered_data.groupby('두께감')['가격'].mean()

# 막대 그래프 그리기
plt.figure(3)
plt.bar(mean_price_by_color.index, mean_price_by_color, color='skyblue')
plt.xlabel('color')  # x축 라벨
plt.ylabel('average price')  # y축 라벨
plt.title('두께감에 따른 평균 가격')  # 제목
plt.show()

filtered_data = data[data['밝기'].isin(['보통이에요', '밝아요', '어두워요'])]
# '색감'에 대한 평균 '가격' 계산
data['가격'] = pd.to_numeric(data['가격'], errors='coerce')
mean_price_by_color = filtered_data.groupby('밝기')['가격'].mean()

# 막대 그래프 그리기
plt.figure(4)
plt.bar(mean_price_by_color.index, mean_price_by_color, color='skyblue')
plt.xlabel('color')  # x축 라벨
plt.ylabel('average price')  # y축 라벨
plt.title('밝기에 따른 평균 가격')  # 제목
plt.show()

# '성별' 열에서 '남', '여'만 추출
df_filtered = data[data['성별'].isin(['남', '여'])]

# '성별'에 대한 평균 '가격' 계산
mean_price_by_gender = df_filtered.groupby('성별')['가격'].mean()

# 막대 그래프 그리기
plt.figure(5)
plt.bar(mean_price_by_gender.index, mean_price_by_gender, color='skyblue')
plt.xlabel('성별')  # x축 라벨
plt.ylabel('평균 가격')  # y축 라벨
plt.title('성별에 따른 평균 가격')  # 제목
plt.show()

# '카테고리'에 대한 평균 '가격' 계산
mean_price_by_category = data.groupby('카테고리')['가격'].mean()

# 막대 그래프 그리기
plt.figure(6)
plt.figure(figsize=(10,6))  # 그래프 크기 설정
plt.bar(mean_price_by_category.index, mean_price_by_category, color='skyblue')
plt.xticks(rotation=45)  # x축 라벨 회전 (카테고리 이름이 길 경우 겹치는 것을 방지)
plt.xlabel('카테고리')  # x축 라벨
plt.ylabel('평균 가격')  # y축 라벨
plt.title('카테고리에 따른 평균 가격')  # 제목
plt.show()

# '바지' 카테고리와 '성별'이 '남', '여'인 행만 포함하는 데이터프레임을 생성합니다.
pants_df = data[(data['카테고리'] == '바지') & (data['성별'].isin(['남', '여']))]

# '성별'에 대한 '바지' 구매 횟수를 계산합니다.
pants_count_by_gender = pants_df['성별'].value_counts()

# 막대 그래프 그리기
plt.figure(7)
plt.bar(pants_count_by_gender.index, pants_count_by_gender, color='skyblue')
plt.xlabel('성별')  # x축 라벨
plt.ylabel('바지 구매 횟수')  # y축 라벨
plt.title('성별에 따른 바지 구매 횟수')  # 제목
plt.show()

# '아우터' 카테고리와 '성별'이 '남', '여'인 행만 포함하는 데이터프레임을 생성합니다.
pants_df = data[(data['카테고리'] == '아우터') & (data['성별'].isin(['남', '여']))]

# '성별'에 대한 '아우터' 구매 횟수를 계산합니다.
pants_count_by_gender = pants_df['성별'].value_counts()

# 막대 그래프 그리기
plt.figure(8)
plt.bar(pants_count_by_gender.index, pants_count_by_gender, color='skyblue')
plt.xlabel('성별')  # x축 라벨
plt.ylabel('아우터 구매 횟수')  # y축 라벨
plt.title('성별에 따른 아우터 구매 횟수')  # 제목
plt.show()

delivery_df = data[data['배송'].isin(['빨라요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '배송' 만족도를 계산합니다.
delivery_satisfaction_by_price = delivery_df.groupby(price_bins)['배송'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(9)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('배송 만족도 비율')  # y축 라벨
plt.title('가격에 따른 배송 만족도')  # 제목
plt.show()

# '카테고리'가 '아우터'이고, '배송'이 '빨라요' 또는 '아쉬워요'인 행만 포함하는 데이터프레임을 생성합니다.
outer_delivery_df = data[(data['카테고리'] == '아우터') & data['배송'].isin(['빨라요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(outer_delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '배송' 만족도를 계산합니다.
delivery_satisfaction_by_price = outer_delivery_df.groupby(price_bins)['배송'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(10)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('배송 만족도 비율')  # y축 라벨
plt.title('가격에 따른 아우터 배송 만족도')  # 제목
plt.show()

# '카테고리'가 '상의'이고, '배송'이 '빨라요' 또는 '아쉬워요'인 행만 포함하는 데이터프레임을 생성합니다.
outer_delivery_df = data[(data['카테고리'] == '상의') & data['배송'].isin(['빨라요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(outer_delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '배송' 만족도를 계산합니다.
delivery_satisfaction_by_price = outer_delivery_df.groupby(price_bins)['배송'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(11)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('배송 만족도 비율')  # y축 라벨
plt.title('가격에 따른 상의 배송 만족도')  # 제목
plt.show()

# '카테고리'가 '바지'이고, '배송'이 '빨라요' 또는 '아쉬워요'인 행만 포함하는 데이터프레임을 생성합니다.
outer_delivery_df = data[(data['카테고리'] == '바지') & data['배송'].isin(['빨라요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(outer_delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '배송' 만족도를 계산합니다.
delivery_satisfaction_by_price = outer_delivery_df.groupby(price_bins)['배송'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(12)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('배송 만족도 비율')  # y축 라벨
plt.title('가격에 따른 바지 배송 만족도')  # 제목
plt.show()

delivery_df = data[data['포장'].isin(['꼼꼼해요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '포장' 만족도를 계산합니다.
delivery_satisfaction_by_price = delivery_df.groupby(price_bins)['포장'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(13)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('포장 만족도 비율')  # y축 라벨
plt.title('가격에 따른 포장 만족도')  # 제목
plt.show()

# '카테고리'가 '아우터'이고, '포장'이 '꼼꼼해요' 또는 '아쉬워요'인 행만 포함하는 데이터프레임을 생성합니다.
outer_delivery_df = data[(data['카테고리'] == '아우터') & data['포장'].isin(['꼼꼼해요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(outer_delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '포장' 만족도를 계산합니다.
delivery_satisfaction_by_price = outer_delivery_df.groupby(price_bins)['포장'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(14)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('포장 만족도 비율')  # y축 라벨
plt.title('가격에 따른 아우터 포장 만족도')  # 제목
# plt.show()

# '카테고리'가 '상의'이고, '포장'이 '꼼꼼해요' 또는 '아쉬워요'인 행만 포함하는 데이터프레임을 생성합니다.
outer_delivery_df = data[(data['카테고리'] == '상의') & data['포장'].isin(['꼼꼼해요', '아쉬워요'])]

# '가격'을 범위별로 나눕니다. 범위는 자유롭게 설정하실 수 있습니다.
price_bins = pd.cut(outer_delivery_df['가격'], bins=[0, 50000, 100000, 150000, np.inf])

# 각 '가격' 범위에서 '포장' 만족도를 계산합니다.
delivery_satisfaction_by_price = outer_delivery_df.groupby(price_bins)['포장'].value_counts(normalize=True)

# 결과를 막대 그래프로 그립니다.
delivery_satisfaction_by_price.unstack().plot(kind='bar', stacked=True)
plt.figure(15)
plt.xlabel('가격 범위')  # x축 라벨
plt.ylabel('포장 만족도 비율')  # y축 라벨
plt.title('가격에 따른 상의 포장 만족도')  # 제목
plt.show()