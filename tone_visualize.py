import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

# 무신사 폰트 경로 설정 (시스템에 설치된 폰트 경로에 따라 수정 필요)
font_path = "C:/Users/weidon/AppData/Local/Microsoft/Windows/Fonts/musinsa-Medium.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 얻어낸 데이터
tones = ["니다","니다요", "아요", "어요", "워요", "해요", "게요", "세요", "네요", "고요", "예요", "에요", "돼요", "되요", "뻐요", "싸요",
        "니당", "슴당", "아용", "어용", "워용", "해용", "게용", "세용", "네용", "고용", "예용", "에용", "돼용", "되용", "뻐용", "싸용", "야징",
        "슴미다", "아욤", "어욤", "워욤", "해욤", "게욤", "세욤", "네욤", "고욤", "예욤", "에욤", "돼욤", "되욤", "뻐욤", "싸욤",
        "아여", "어여", "워여", "해여", "게여", "세여", "네여", "고여", "예여", "에여", "돼여", "되여", "뻐여", "싸여",
        "좋음", "조음", "괜찮음", "적당함", "낫밷", " 쌈", "비쌈", "딱임", "굿", "굳", "구웃", "구욷"
        "..", ",,", "!", "ㅠㅠ", "ㅜㅜ", "~", "ㅎㅎ", "ㅋㅋ", "^^",]
male_count = {'니다': 220114, '니다요': 688, '아요': 145979, '어요': 58396, '워요': 6756, '해요': 26672, '게요': 10052, '세요': 12927, '네요': 109015, '고요': 4967, '예요': 1949, '에요': 19113, '돼요': 565, '되요': 497, '뻐요': 24607, '싸요': 53, '니당': 6403, '슴당': 68, '아용': 3395, '어용': 1342, '워용': 153, '해용': 604, '게용': 518, '세용': 830, '네용': 2830, '고용': 79, '예용': 33, '에용': 425, '돼용': 9, '되용': 25, '뻐용': 872, '싸용': 1, '야징': 92, '슴미다': 20, '아욤': 122, '어욤': 44, '워욤': 1, '해욤': 19, '게욤': 5, '세욤': 38, '네욤': 141, '고욤': 4, '예욤': 6, '에욤': 14, '돼욤': 1, '되욤': 2, '뻐욤': 29, '싸욤': 1, '아여': 3151, '어여': 778, '워여': 83, '해여': 743, '게여': 490, '세여': 612, '네여': 3346, '고여': 205, '예여': 42, '에여': 601, '돼여': 29, '되여': 19, '뻐여': 371, '싸여': 7, '좋음': 3854, '조음': 96, '괜찮음': 329, '적당함': 273, '낫밷': 15, ' 쌈': 22, '비쌈': 9, '딱임': 182, '굿': 9496, '굳': 3414, '구웃': 67, '구욷..': 0, ',,': 1273, '!': 70477, 'ㅠㅠ': 2763, 'ㅜㅜ': 950, '~': 23108, 'ㅎㅎ': 14754, 'ㅋㅋ': 2784, '^^': 3691}
female_count = {'니다': 45972, '니다요': 161, '아요': 60276, '어요': 39048, '워요': 6277, '해요': 15437, '게요': 1843, '세요': 3683, '네요': 21593, '고요': 2461, '예요': 2337, '에요': 10828, '돼요': 471, '되요': 159, '뻐요': 21121, '싸요': 23, '니당': 6712, '슴당': 67, '아용': 3748, '어용': 2401, '워용': 514, '해용': 754, '게용': 259, '세용': 435, '네용': 1761, '고용': 67, '예용': 103, '에용': 551, '돼용': 24, '되용': 16, '뻐용': 1781, '싸용': 1, '야징': 70, '슴미다': 19, '아욤': 249, '어욤': 168, '워욤': 13, '해욤': 42, '게욤': 10, '세욤': 40, '네욤': 167, '고욤': 4, '예욤': 8, '에욤': 50, '돼욤': 1, '되욤': 0, '뻐욤': 132, '싸욤': 0, '아여': 1703, '어여': 792, '워여': 122, '해여': 474, '게여': 113, '세여': 311, '네여': 979, '고여': 105, '예여': 52, '에여': 443, '돼여': 14, '되여': 6, '뻐여': 526, '싸여': 6, '좋음': 1478, '조음': 168, '괜찮음': 132, '적당함': 90, '낫밷': 1, ' 쌈': 9, '비쌈': 4, '딱임': 105, '굿': 2868, '굳': 841, '구웃': 32, '구욷..': 0, ',,': 2324, '!': 41542, 'ㅠㅠ': 4397, 'ㅜㅜ': 1357, '~': 12770, 'ㅎㅎ': 7354, 'ㅋㅋ': 2259, '^^': 2202}

# 데이터 전처리
total_male_count = sum(male_count.values())
total_female_count = sum(female_count.values())
rated_male_count = {key: male_count[key] / total_male_count for key in tones}
rated_female_count = {key: female_count[key] / total_female_count for key in tones}
sorted_male = sorted(rated_male_count.items(), key=lambda x: x[1], reverse=True)
sorted_male = sorted_male[:30]
sorted_female = sorted(rated_female_count.items(), key=lambda x: x[1], reverse=True)
sorted_female = sorted_female[:30]
rs_tones = list()
for tone in sorted_male:
    rs_tones.append(tone[0])
for tone in sorted_female:
    if tone[0] not in rs_tones:
        rs_tones.append(tone[0])
refacted_male = {key: rated_male_count[key] for key in rs_tones}
refacted_female = {key: rated_female_count[key] for key in rs_tones}

# 시각화를 위한 데이터 가공
male_values = list(refacted_male.values())
female_values = list(refacted_female.values())

# 그래프 크기 설정
plt.figure(figsize=(12, 6))

# 막대 그래프 그리기
bar_width = 0.35
bar_male = np.arange(len(rs_tones))
bar_female = bar_male + bar_width

plt.bar(bar_male, male_values, width=bar_width, label='남성', alpha=0.7)
plt.bar(bar_female, female_values, width=bar_width, label='여성', alpha=0.7)

# 그래프에 레이블 추가
plt.xlabel('리뷰톤')
plt.ylabel('빈도')
plt.title('성별에 따른 리뷰톤 분포')
plt.xticks(bar_male + bar_width/2, rs_tones, rotation=45, ha='right')
plt.legend()

# 그래프 보여주기
plt.tight_layout()
plt.show()