#second.py
import streamlit as st

st.title("2번 페이지")

#2번 페이지에서 1번 페이지로 이동!
st.page_link("pagelink.py",
              label="1번 페이지로 가기",
              icon="🚕")

st.write(st.session_state['로그인아이디']) 
st.write(st.session_state['이름']) 