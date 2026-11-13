# 파일명: dataEx.py
import pandas as pd     # 분석 도구!
import streamlit as st  # 웹 사이트 만들기

주문 = {
    "주문번호": [2001, 2002, 2003, 2004, 2005, 2006, 2006],
    "메뉴": ["아메리카노", "카페라떼 ", "크로플", "딸기스무디", "카페라떼", "아메리카노", "아메리카노"],
    "수량": [1, 2, 1, 99, 2, 1, 1],
    "가격": [4500, 5000, 6500, 6000, 5000, 4500, 4500],
    "결제수단": ["카드", "현금", None, "카드", "카드", None, None],
}
df = pd.DataFrame(주문)

# # 빈 값 처리
# # dropna() : 빈 값이 있는 행을 삭제!
# # fillna(값): 빈 값을 다른 값으로 채움!
# #   둘다 새 표를 돌려준다.(원본은 그대로)

# # 주문 통계에서 결제 수단이 비어있을 때 주문을 빼버리면
# # 매출이 줄어든다. 값은 채우고 매출은 유지한다.

# # 전체 행수를 출력!

# # 전체적인 내용 확인
# #print(df)
# # 1. 안전하게 원본을 복사한다.
# 새표 = df.copy()

# # 2. 새로운 복사된 표를 먼저 결제수단 열을 가져온다
# #
# 새표["결제수단"] = 새표["결제수단"].fillna("미확인")

# # 3. 확인
# #print(새표)
# #----------------------------------------------
# st.title("데이터 분석")
# st.header("카페 주문 데이터")
# # 원본 데이터 출력
# st.dataframe(df)
# st.write(" 전체 행 수: ",len(df))

# st.subheader("빈 값 처리 결과")
# st.dataframe(새표)
# st.write("처리 후 행 수:", len(새표))


# # 스트림릿을 공부X -> HTML,CSS,JS,React
# # 1. 저장해야하는 데이터
# # 2. 실행하는 순서

# #------------------------------------------
# # 중복 제거
# # duplicated : 중복인지 확인
# # drop_duplicates: 중복제거

# # 모든 열이 같은 중복 행 확인
# # 웹 화면에 소주제 글씨 보여줘!
# st.subheader("중복 확인")
# # 스트림릿이 True,False 타입 Bool
# #st.write(새표.duplicated())

# print(새표.duplicated())

# # 중복 확인 개수 세기
# print("중복 확인:", 새표.duplicated().sum())

# # 중복 제거
# print("중복 제거: ", df.drop_duplicates())
# print(df)

# print(새표)

# # 위에서 아래로 가며 행마다 "앞에 모든 열이 똑같은 행이 있었나"
# # 처음나온 행 False 두번째 True 비교하고 다르면 False

# # 자주 사용하는 옵션
# # 주문 번호가 같으면 중복
# df.drop_duplicates(subset=["결제수단"])

# # 마지막 것을 남긴다.
# df.drop_duplicates(keep="last")

# # 중복된 행을 전부 삭제
# df.drop_duplicates(keep=False)

# # 코드를 작성할 때 순서
# # 1. duplicated()
# # 2. .sum() 개수 세기
# # 3. drop_duplicates()
# # 4. 기존 길이와 중보제거된 길이 확인

#-----------------------------------------
# 공백 지우기
#  - 공백 때문에 세어지는 값

주문 = {
    "주문번호": [2001, 2002, 2003, 2004, 2005, 2006, 2006],
    "메뉴": ["아메리카노", "카페라떼 ", "크로플", "딸기스무디", "카페라떼", "아메리카노", "아메리카노"],
    "수량": [1, 2, 1, 99, 2, 1, 1],
    "가격": [4500, 5000, 6500, 6000, 5000, 4500, 4500],
    "결제수단": ["카드", "현금", None, "카드", "카드", None, None],
}
df = pd.DataFrame(주문)

새표 = df.copy()
# 공백제거 할 때 사용하는 기능
# 1. 어떤 열을 선택? 메뉴
# 2. strip() : 앞 뒤 공백 제거한다.
#    글자 열에만 사용된다.

# 데이터 한줄을 가지고 와서 그 안에 문자들
# str 그 안에 공백을 제거해주세요!
print(새표["메뉴"].str.strip())

# 공백이 제거 되었는지 잘 모르겠다!
# value_counts()
# - 값 별로 개수를 센다
# - 열에 들어있는 메뉴 이름 하나 하나
print(새표["메뉴"].value_counts())

# copy()	원본과 복사본
# dropna() / fillna()	빈 값 삭제 / 빈 값 채우기
# duplicated() / drop_duplicates()	중복 확인 / 중복 제거
# drop_duplicates() / drop_duplicates(keep="last") / drop_duplicates(keep=False)	첫 번째 유지 / 마지막 유지 / 중복된 행 전부 삭제
# drop_duplicates() / drop_duplicates(subset=["메뉴"])	모든 열 기준 / 특정 열 기준
# str.strip()	문자열 앞뒤 공백 제거
# value_counts() / count() / len()	값별 개수 / 빈 값 제외 개수 / 빈 값 포함 개수
# duplicated().sum()	중복으로 표시된 행 개수
# print() / st.write() / st.dataframe()	터미널 출력 / 웹 화면 출력 / 웹 표 출력

# 위에 있는 함수들의 차이점을 찾아보세요~