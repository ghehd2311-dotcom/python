# zombie_game.py
# PRD(Product Requirements Document)문서
#  - 무엇을 만들지
# 1. 어떤 서비스 인가요? (한 줄 목적)
#  - 내 체력(HP)을 입력하면 , 좀비 앞에서 싸울지/도망갈지
#    를 글자와 확률로 알려준다.

# 2. 누가 사용하나요?
#  - 좀비 게임에서 캐릭터의 행동을 예측해 보고싶은 사람

# 3. 사용자는 어떻게 사용하나요?
#  -1. 현재 체력을 0~ 100사이로 입력한다.
#  -2. 싸울까? 도망갈까? 버튼을 누른다.
#  -3. 싸움을 선택할 확률과 예상 행동을 확인한다.

# 4. 어떤 데이터로 학습하나요?
#  - 과거 플레이어의 체려과 실제 선택을 사용한다.

import streamlit as st
from sklearn.linear_model import LogisticRegression

# ---- 과거 기록 ----
체력 = [[10], [20], [30], [70], [80], [90]]                    # 힌트: 내 체력(HP)
행동 = ["도망", "도망", "도망", "싸운다", "싸운다", "싸운다"]       # 정답

# ---- 화면 ----
st.title("🧟 좀비 게임, 싸울까 도망갈까?")
입력체력 = st.number_input("내 체력(HP)", min_value=0, max_value=100, value=50)

# ---- 공부시키기 ----
모델 = LogisticRegression()
모델.fit(체력, 행동)


if st.button("예측하기"):
    결과 = 모델.predict([[입력체력]])                       # 답 (글자)
    확률 = 모델.predict_proba([[입력체력]])                 # 종류별 확률
    싸움칸 = list(모델.classes_).index("싸운다")            # "싸운다" 칸 번호 찾기
    싸움확률 = float(확률[0][싸움칸])                       # 0~1

    if 결과[0] == "싸운다":
        st.write("⚔️ 좀비와 싸울 것 같아요!")
    else:
        st.write("🏃 도망갈 것 같아요!")

    st.write("싸울 확률:", round(싸움확률 * 100), "%")