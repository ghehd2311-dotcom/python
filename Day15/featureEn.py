# featureEn.py
# 특성(힌트)공학(바꾸다) = AI가 알아보기 쉽게 힌트를 바꾸는 일
# 1. 섞기
# 2. 글자를 숫자로
# 3. 빼기

# 편의점.csv 파일을 다운로드 해서 data폴더 안으로 집어넣으세요!
# # 1.도구
# # csv파일을 불러오기 ,예측
import pandas as pd

# # 모델,학습,예측,채점

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 데이터
#  파일 읽어야되는데 파일의 위치가 변경
#  같은 폴더에 편의점.csv랑 featureEn.py  = 파일명.csv
#  다른 폴더 data 폴더 안에 있고 featureEn.py Day15 = 파일명으로
#  못 읽는다.

# 파이썬에서 경로는 현재 실행중인 파일의 폴더 기준으로 찾는다
# 기준 Day15 폴더 안이다!
데이터 = pd.read_csv("data/편의점.csv")

#print(데이터.head(3)) 확인하고 끝!

# 힌트3개만
# [] 괄호가 없다! 생길수있는 에러의 타입은?
# KeyError : 그런 열이 없다
# 여러개의 열 이름 목록을 한 번더 대괄호고 감싼다
X = 데이터[["개당가격","개수","계산대번호"]]
y = 데이터["총금액"]

# 학습용/시험용 나누기
X_train,X_test,y_train,y_test = train_test_split(X,
                                                 y,
                                                 test_size=0.2,
                                                 random_state=1)

모델 = LinearRegression()
모델.fit(X_train,y_train)

예측 = 모델.predict(X_test)

print()

# 기준선
# 평균만 찍기
평균 = y_train.mean()
print(평균)
기준선예측 = [평균] * len(y_test)
print("[기준선] 평균만 찍기 평균 오차:",round(mean_absolute_error(y_test,기준선예측)))


print(" 평 균 : ", 예측.mean())
print()
print("[섞기 전] :평균 오차 : "
        ,round(mean_absolute_error(y_test,예측)))