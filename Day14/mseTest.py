#mseTest.py

#MAE 틀린 평균을 낸다
#MSE 틀린 크기에 제곱해서 평균을 낸다.
#  큰 실수를 휠씬 크게 벌 준다
# Mean Squared Error

import pandas as pd
import streamlit as st

from sklearn.metrics import mean_absolute_error,mean_squared_error

# 실제 = [30, 30, 30, 30]
# A예측 = [32, 32, 32, 32]
# B예측 = [30, 30, 30, 38]

# # mean_absolute_error
# # 실제값,예측값을 비교해서 평균 얼마나 틀렸는지 계산
# # 하는 함수

# print("A MAE:", mean_absolute_error(실제, A예측))
# print("B MAE:", mean_absolute_error(실제, B예측))

# 오차 = [abs(a - b) for a, b in zip(실제, B예측)]
# print("가장 큰 오차:", max(오차))

# MSE가 없으면
# - 평균이 같은 모델의 차이를 못봄
# - 큰 실수를 찾으려 코드를 따로 짬
# - 사고 난 뒤에야 문제를 암

# MSE가 있으면
# - 큰 실수를 막을 수 있음
# - 지표 하나로 한번에 비교
# - 배포 전에 위험을 걸래냄

# 응급실 환자 수 예측
# 약국 약 재고 예측
# 전력 수요 예측
# 폭염, 태풍 피해 예측

# 모델이 여러 개 일 떄 점수로 비교해서 더 좋은
# 모델을 고르기!
# 숫자 하나로 이 모델이 얼마나 틀리는가?(MAE,MSE)
# 점수가 낮을 수록 좋은 모델!
# 오차 = 정답과 예측이 얼마나 다른가?
# 오차의 평균 (틀린만큼 벌준다)
# 오차의 제곱한 값의 평균(크게 틀릴 수록 벌점을 휠씬 크게 준다.)

# 학습하고 예측한 값들!
# 현재 정답은 10 기준
A모델 = [9,11,9,11]   #틀린정도 [1,1,1,1]
B모델 = [10,10,10,14] #틀린정도 [0,0,0,4]

# 확인 검증! MSE
# A : (1+ 1 + 1+1) / 4 = 1점
# B : (0+0+0+4) / 4 = 1점

# 규칙 현재값에 제곱을 해서 평균!
# A : (1x1 + 1x1 + 1x1 + 1x1 ) /4 = 1점
# B : (0x0 + 0x0 + 0x0 + 4x4 ) /4 = 4점

# 실행순서
# 1. 정답과 모델별 예측값을 준비한다.
# 2. 모델마다 오차 점수(MAE,MSE) 계산한다.
# 3. 점수를 비교한다
# 4. 점수가 낮은 모델을 선택한다.

정답 = [10,10,10,10]
A모델 = [9,11,9,11]   #틀린정도 [1,1,1,1]
B모델 = [10,10,10,14] #틀린정도 [0,0,0,4]

print()
print("A mae: ", mean_absolute_error(정답,A모델))
print("B mae: ", mean_absolute_error(정답,B모델))

print()
print("A mse: ", mean_squared_error(정답,A모델))
print("B mse: ", mean_squared_error(정답,B모델))

print()
mse_a = mean_squared_error(정답,A모델)
mse_b = mean_squared_error(정답,B모델)

print("선택된 모델: " ,"A" if mse_a < mse_b else "B" )
# 현업에서는 데이터가 수천 수백건 이기 때문에 numpy
# 예측값은 직접 적지 않고! model.predict(데이터)로 모델이 만들어진값
# 비교할 때는 기준선(baseline)을 꼭 둔다.
# 점수가 낮다고 바로 확정하지 않는다.(속도,비용,안정성)

# 치킨집 주문량 예측!
# 치킨집의 하루 실 주문량 [20,30,40]
정답 = [20,30,40]
X모델 = [22,28,42]
Y모델 = [20,30,46]

# 각 모델의 MAE,MSE를 출력!
# X모델 MAE : **  MSE : **
# Y모델 MAE : **  MSE : **
print("X  MAE:", mean_absolute_error(정답, X모델), " MSE:", mean_squared_error(정답, X모델))
print("Y  MAE:", mean_absolute_error(정답, Y모델), " MSE:", mean_squared_error(정답, Y모델))

# 수요예측(주문량,판매량,재고 발주)

#배달 시간 예측 오차가 2배가 되면 점수?
# 실제 데이터 - 실제 배달 시간 4건
정답 = [30, 30, 30, 30]

x예측 = [32, 34, 38]
y예측 = [30, 30, 30,50]

# 입력을 바꿔가면서 어떻게 변하는지 본다
# 서비스 운영중에는 오차 점수를 매일 계산해 그래프로
# 모니터링
# 점수가 오른 원인은 데이터 오류,시장변화,모델 노후화
# 다양하게 점수는 " 문제를 찾으러갈 신호"
for x in [32, 34, 38]:
    예측 = [30, 30, 30,x]
    print(x ,"MAE: ",mean_absolute_error(정답,예측),
             " MSE: ",mean_squared_error(정답,예측))