#main.py
# 항상 스트림릿은 main파일에서 실행!
# streamlit run main.py


import streamlit as st
import sqlite3 as db

db저장소 = db.connect("kakao.db")
마우스 = db저장소.cursor()

마우스.execute("""
    create table if not exists members(
        회원번호   integer  primary key  autoincrement,
        아이디     text     not null  unique,
        비밀번호   text     not null,
        이름       text     not null,
        전화번호   text     not null  unique
    )
""")

# 웹페이지끼리 정보 공유하는 세션!
# 세션 칸 만들기
if "로그인한유저" not in st.session_state:
    st.session_state["로그인한유저"] = None


st.title("💛 카카오 로그인")

아이디 = st.text_input("아이디").strip()
비밀번호 = st.text_input("비밀번호", type="password").strip()

if st.button("로그인"):
    마우스.execute(f"""
        select * from members
        where 아이디 = '{아이디}' and 비밀번호 = '{비밀번호}'
    """)
    회원 = 마우스.fetchone()

    if 회원 == None:
        st.warning("아이디 또는 비밀번호를 확인해주세요")
    else:
        st.session_state["로그인한유저"] = 회원
        st.switch_page("pages/2_채팅목록.py")

st.page_link("pages/1_회원가입.py", label="아직 회원이 아니라면? 회원가입")