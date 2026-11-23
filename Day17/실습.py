
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# 과거 기록(힌트 : 링크 , 스)
# 링크 = [[0], [1], [2], [6], [7], [8]]
# 스팸 = ["정상", "정상", "정상", "스팸", "스팸", "스팸"]

# 모델 = LogisticRegression()
# 모델.fit(링크,스팸)


# st.title("스팸일까요?(로지스틱)")
# 입력개수  = st.number_input("이동거리 (km)",value=0,min_value=0)

# if st.button("스팸 확인"):
#     결과 = 모델.predict([[입력개수]])
#     확률 = 모델.predict_proba([[입력개수]])
#     스팸인덱스 = list(모델.classes_).index('스팸')
    
#     if 결과[0] == "스팸":
#         st.write("스팸 메일 갔어요!")
#     else:
#         st.write("정상 메일 갔어요!")

#     print('스팸확률: ', 확률[0][스팸인덱스])


안한날 = [[1], [2], [3], [8], [9], [10]]
해지 = ["유지", "유지", "유지", "해지", "해지", "해지"]

모델 = LogisticRegression()
모델.fit(안한날,해지)

st.title("- 음악 , 영상 구독 서비스가 :이 사용자가 해지할까??(로지스틱)")
접속안한날  = st.number_input("접속 안한날 ",value=0,min_value=0)

if st.button("확인"):
    결과 = 모델.predict([[접속안한날]])
    확률 = 모델.predict_proba([[접속안한날]])
    유지인덱스 = list(모델.classes_).index('유지')
    
    if 결과[0] == "유지":
        st.write(접속안한날, "유지 했어요!")
    else:
        st.write(접속안한날, "해지 했어요!")

    st.write('유지 확률: ', 확률[0][유지인덱스])
    