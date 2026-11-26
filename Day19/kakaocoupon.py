# kakaocoupon.py

# 내가만든 모듈 가져오기
import my

# my하는 모듈 안에 스트림릿 타이틀!
my.st.title("쿠폰 보내기")

# 테이블 제약조건 넣어서 생성하기!
# 테이블명 : coupons

# 선물하기에서 선물을 보내면 선물번호가
# 자동으로 생긴다.
# 보내는사람 아이디,받는 사람아이디, 전화번호
# 상품 이름은 꼭! 있어야된다.
# 받는 사람은 쿠폰 번호로 상품을 받는다
# 쿠폰번호는 절대 겹치면 안되고 값이 꼭!
# 있어야된다.
# 카드 메서지는 안 써도 된다.

# 데이터 타입, 제약조건, 생성하는 코드
# 필수 : 보내는사람아이디,받는아아디
#        받는사람의전화번호(중복)
#        상품이름,쿠폰번호(중복)
# 선택 : 카드메시지

# 혹시 쿠폰 보내기를 하려면 로그인이 필요하다
# 내가 로그인이 되어있니?
#  친구목록을 조회해야되니 로그인확인

db저장소 = my.db.connect("kakao.db")
#2. 조작도구 만들기
마우스 = db저장소.cursor()


my.st.subheader("로그인 실습")
로그인탭,가입탭 = my.st.tabs(["로그인","회원가입"])

# 로그인탭을 누르면 로그인할 수있는 화면
with 로그인탭:
    # 사용자 입력받음
    아이디 = my.st.text_input("아이디", key="로그인_아이디").strip()
    비밀번호 = my.st.text_input("비밀번호", type="password", key="로그인_비번").strip()

    # 디비 조회
    마우스.execute(f"""
        select
            *
        from
            members
        where
            아이디 = '{아이디}' and  비밀번호 = '{비밀번호}'
    """)
    회원 = 마우스.fetchone()

    if 회원 == None:
        my.st.warning("아이디 또는 비밀번호를 확인해주세요")
    else:
        my.st.write("찾은 아이디:" , 회원)
        my.st.session_state['로그인한유저'] = 회원
        my.st.page_link('pages/database.py',label='채팅방으로 이동')




# 가입탭 누르면 가입창이 뜬다
with 가입탭:
    # 사용자 입력받음
        아이디 = my.st.text_input("아이디", key="회원가입_아이디").strip()
        비밀번호 = my.st.text_input("비밀번호", type="password", key="회원가입_비번").strip()
        이름 = my.st.text_input("이름", key="회원가입_이름").strip()
        전화번호 = my.st.text_input("전화번호", key="회원가입_전화번호").strip()
    
        if my.st.button("가입"):
            # 디비 조회
            마우스.execute(f"""
                insert into members(아이디, 비밀번호, 이름,전화번호)
                values('{아이디}','{비밀번호}','{이름}','{전화번호}')
            """)
            db저장소.commit()


# 파이썬에서 데이터를 가져올 때
# 튜플(tuple)
#  - 리스트랑 똑같다!
#  - 여러개를 저장할 수있다. 0번부터 데이터를
#   1씩 증가하면서 저장한다.
#  - (값1,값2,...) 괄호
#  - 튜플은 한번 데이터가 저장되면 수정,삭제 불가

# 마우스.fetchone()
#  데이터베이스에 한 줄의 결과 (Row)

# 마우스.fetchall()
# 데이터베이스에서 여러 줄 결과


    #(1,qwer,qwer11!,이서희,010-1111-1111)
    # if 회원[2] == 내가입력한비밀번호:
    #     my.st.success("로그인성공")
    # else:
    #     my.st.error("틀렸는데?")
    # if문을 직접 작성하다 오류를 일으킬 수있다.