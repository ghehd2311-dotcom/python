# pagelink.py
# 모든 서비스의 기본 기능 4가지
#  - CRUD
#  - Create (만들기)
#  - Read (읽기)
#  - Upate (고치기)
#  - Delete ( 지우기 )

#페이지이동
# - 페이지(page) + 연결(link)
# -  누르면 다른 페이지로 가는 링크!
import streamlit as st

st.title("1번 페이지")

# page_link("페이지경로")
# 현재 실행중인 pagelink.py 위치를 기준으로
# 경로를 찾는다
# streamlit으로 여러 페이지를 이동시키고
# 싶을 경우에는 pages폴더를 만든다. pages이름이
# 지정되어있다. 파이썬 파일 이름은 자유롭게 지정가능함

st.page_link("pages/second.py",
              label="2번 페이지로 가기",
              icon="🚕")

# 현재 페이지에서 로그인한 아이디를 2번 페이지로 이동!
# 로그인아이디 변수는 현재 파일에서만 사용이 가능하다
# 다른 페이지로 이동이 불가능하다!

# session
# - 내가 사이트에 들어와있는 동안  나를 기억해주는것
# - 사이트들끼리 정보를 공유할 수있다.

# session_state()
#  - session(접속해 있는 동안) + state(상태)
#  - 페이지를 이동해도 지워지지 않는 상자 (딕션너리)
#  - key 와 value 이루어져있다.

로그인아이디 = "eryna"
이름 = '백호동'
st.session_state["로그인아이디"] = 로그인아이디
st.session_state['이름'] = 이름


st.write(로그인아이디)