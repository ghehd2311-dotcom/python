# app3.py

import streamlit as st

# python -m streamlit run app3.py

st.header("LLM들은 확률로 고른다")
st.write("확률로 고르기 때문에 답변이 똑같지 않다!")

st.title("3사 모델 비교")

# 화면을 3칸으로 나누기
칸1 , 칸2, 칸3 = st.columns(3)

with 칸1:
    st.subheader("GPT")
    st.write("👍 기능이 다양하고, 쓰는 사람과 자료가 많다")
    st.write("👎 모델 종류가 자주 바뀌어서 헷갈린다")
    st.write("👎 칭찬이 과하다는 지적이 있었다 (OpenAI가 줄이는 업데이트를 함)")

with 칸2:
    st.subheader("Claude")
    st.write("👍 긴 문서 정리, 자연스러운 글, 코드 작업")
    st.write("👍 행동 원칙을 자세히 공개")
    st.write("👎 무료로 쓸 수 있는 양이 적은 편")

with 칸3:
    st.subheader("Gemini")
    st.write("👍 구글 서비스(지메일, 드라이브, 문서)와 연결")
    st.write("👍 사진, 영상, 음성까지 다루기 (멀티모달)")
    st.write("👎 구글 서비스를 안 쓰면 장점이 줄어든다")