# Streamlit
# - 파이썬으로 웹사이트나 웹 애플리케이션을 쉽게
#   만들수있게 도와주는 도구!

# 설치
# pip install streamlit

#설치 확인
# streamlit --version

# AI -> 머신러닝 기초

#1.현재 파일이 실행될때 import 도구명
#  현재 streamlit 도구 안에 있는 기능들을 내가
#  다 사용하겠음!
# as 줄임말
import streamlit as st

st.title("AI 리터러시 수업!")
st.header("Ai란?")
st.write("컴퓨터가 사람의 지능적인 작업을 수행하도록 만드는 기술!")

st.image("./images/1_ai.png", caption="AI란?")

#2. 위에 내용을 실행!
# 내 컴퓨터 안에서만 볼 수있는 웹사이트 실행!
# streamlit run 파일명.py
# 터미널켜고 -> cmd -> python -m streamlit run app.py
#3. 항상 코드를 작성하고 나면!! 꼭! 저장하기
# ctrl + s

st.header("규칙 기반 AI란?")
st.write("Rule-Based AI")
st.write("사람이 정한 규칙을 따르는 인공지능")
st.image("./images/1-1_rule.png")

# 머신러닝
st.header("머신러닝(Machine Learning)")
st.write("데이터에서 규칙이나 패턴을 학습하는 기술")
st.write("사람이 모든 규칙을 직접 작성하지 않고 컴퓨터 데이터를 보고 패턴을 찾는다.")
st.image("./images/2_ml.png")

st.header("딥러닝(Deep Learning)")
st.write("복잡한 데이터에서도 특징과 패턴을 학습할 수 있는 기술")
st.write("얼굴인식, 음성인식, 제품불량 이미지 판별, 의료 영상 분석지원")
st.write("여러 층의 인공신경망을 이용하는 머신러닝 기술")
st.image("./images/3_dl.png")

#생성형 AI란?
st.header("생성형 AI란?")
st.write("Generative AI")
st.write("사람이 만든 데이터를 학습하여 새로운 데이터를 생성하는 인공지능")
st.write("텍스트, 이미지, 영상, 음성 등 다양한 형태의 데이터를 생성할 수 있다.")
st.image("./images/4_genai.png")

#LLM이란?
st.header("LLM이란?")
st.write("Large Language Model")   
st.write("대규모 언어 모델")
st.write("사람이 만든 텍스트 데이터를 학습하여 새로운 텍스트를 생성하는 인공지능")
st.image("./images/5_llm.png")