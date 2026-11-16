import streamlit as st
import pandas as pd

# 머신러닝 도구 모델을 가져오는 import
from sklearn.linear_model import LinearRegression

표 = pd.DataFrame({"곡수": [1,2,3], "요금":[500, 1000, 1500]})
x = 표[["곡수"]]
y = 표['요금']

model = LinearRegression()
model.fit(x,y)


st.write('메뉴 1개당 가격(기울기): ', model.coef_[0])
st.write('배달비(절편): ', model.intercept_)
st.number_input('곡수', value= 1)
표['모델 예상']= model.predict(x)
st.write(표)