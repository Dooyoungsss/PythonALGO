import pandas as pd #pandas: 데이터 조작 및 분석을 위한 기초 library
import matplotlib.pyplot as plt #matplotlib: 데이터 시각화를 위한 라이브러리
import seaborn as sns #seaborn: 통계적 데이터 시각화를 위한 라이브러리

#한글 폰트 설정(시각화시에 한글깨짐 방지)
plt.rcParams['font.family'] = 'NanumGothic' #시스템에 해당폰트 설치 확인

#CSV파일 불러오기 (df: data frame)
#cp949 : 한글 인코딩 문제를 해결하기위한 default 셋팅
df = pd.read_csv('서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv', encoding = 'cp949')

#5개 행 출력 (head)
print(df.head())

#열 이름 확인 (df.columns)
print("Column Name:", df.columns)

print('--------------------------------------------')
#데이터 타입 및 결측치 확인(df.info())
print(df.info())

print('#특정 열 예시 보기')
print(df[['호선명', '지하철역', '06시-07시 승차인원', '06시-07시 하차인원']].head())