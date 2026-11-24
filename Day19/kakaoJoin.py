# kakaojoin.py

import sqlite3 as db
import streamlit as st

#1. 저장소 만들기

db저장소 = db.connect("kakao.db")
#2. 조작도구 만들기
마우스 = db저장소.cursor()

# 3. 카카오톡 회원가입 페이지만든다.
#  아이디,비밀번호,이름,전화번호는 꼭 입력한다.

# 칸마다 3질문
# 이 칸으로 정확히 한 사람을 가리키나?
# 이 칸이 비어있으면 안되나?
# 이 칸이 다른사람이랑 겹치면 안되나?

# 데이터베이스에서 테이블을 관리하기 위해서
# 카톡 비유 친구,쇼핑,선물하기 등등
# 회원 테이블을 같이 쓴다.
# 오픈채팅탭 개발자가 비어있는값을 확인하는 if문
# 까먹음?

# 제약 조건 종류
# primary key (대표키)
# not null
#   - 이 칸은 비우면 안됨!
# unique
#  - 이 칸은 겹치면 안된다(중복데이터X)
# 규칙은 칸마다 다르다

# 대표키를 작성할 때는 대부분 숫자로 작성 (uuid)
# 문자는 중복이 발생할 확률이 높음!

마우스.execute("""
    create table if not exists members(
        회원번호   integer  primary key  autoincrement,
        아이디     text     not null  unique,
        비밀번호    text    not null,
        이름       text     not null,
        전화번호    text    not null  unique
    )
""")
# not null 만 컬럼에 지정하면 값을 필수!
#  중복되는 값들이 들어올 수있다.
# unique 로 중복되면 안 되는 칸들에 추가 설정한다!
# 모든 데이터를 저장하는 테이블에 대표 번호
# DB관리자(성능,백업,튜닝,권한,계정관리) - DBA
# OCP 자격증
# 제약조건을 꼭 확인한다.

st.title("카카오 회원가입")
아이디 = st.text_input("아이디").strip()
비밀번호 = st.text_input("비밀번호", type="password").strip()
이름 = st.text_input("이름").strip()
전화번호 = st.text_input("전화번호 (예: 010-1234-5678)").strip()

# 입력값들은 공백이 들어가면 문제가 발생할 수있다!

if st.button("가입하기"):
    마우스.execute(f""" 
    INSERT INTO 
        MEMBERS(아이디, 비밀번호, 이름, 전화번호)
    VALUES 
        ('{아이디}','{비밀번호}','{이름}','{전화번호}')
    """)
    
db저장소.commit()
