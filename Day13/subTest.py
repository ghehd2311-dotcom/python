# subTest.py
#  친구 5명 하루에 몇시간 공부하면 점수가 몇점이야?
#  기록 보고 처음 보는 사람이 몇 점을 받을까?
#  시험 점수를 예측하는 모델

import streamlit as st
import pandas as pd

# 머신러닝 도구 모델을 가져오는 import
from sklearn.linear_model import LinearRegression

#1. 데이터
#  공부시간  점수
공부 = pd.DataFrame({"시간": [1, 2, 3, 4, 5], "점수": [52, 58, 71, 78, 88]})

# X = 표 모양 시간
# Y = 점수(정답)

X = 공부[["시간"]]
Y = 공부["점수"]

# 학습 : 컴퓨터가 규칙을 찾는다
model = LinearRegression()
model.fit(X,Y)

# 예측: 내 예상이 아니라 컴퓨터가 채운다.
공부["모델 예상"] = model.predict(X)

# 차이 평균!
공부["차이 크기"] = (공부["점수"] - 공부["모델 예상"]).abs()

st.write(공부)

mae = 공부["차이 크기"].mean()

st.write("MAE 평균적으로 틀린시간:", f"{mae:.1f}분")