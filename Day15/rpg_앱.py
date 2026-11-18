import os
import random

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

from sprite import 장면_svg   # 도트 캐릭터를 그려 주는 함수 (선생님이 준 파일)

st.set_page_config(page_title="스탯 찍기 게임", layout="centered")

# ---------- 화면 꾸미기 (RPG 느낌) ----------
st.markdown("""
<style>
.stApp {background:#1b1410;}
[data-testid="stSidebar"] {background:#241810;}
header[data-testid="stHeader"] {background:#1b1410;}
h1,h2,h3,p,span,label,div {color:#f0dfb0;}
[data-testid="stVerticalBlockBorderWrapper"] {
  background:linear-gradient(180deg,#4a3422,#33241a);
  border:3px solid #b8924a !important; border-radius:6px; padding:8px;}
.stat {font-family:Georgia,serif; font-size:24px; letter-spacing:3px; color:#e8cf94; font-weight:bold;}
.val {display:inline-block; min-width:52px; text-align:center; background:#241810; border:2px solid #7a5a30;
      color:#fff; font-size:22px; padding:2px 10px; font-family:monospace;}
.bar {height:20px; background:#241810; border:2px solid #7a5a30; margin:4px 0;}
.hp {height:100%; background:linear-gradient(90deg,#8e1b1b,#e04040);}
.mp {height:100%; background:linear-gradient(90deg,#1b3f8e,#4a8be0);}
.big {font-size:44px; font-weight:bold; color:#ffd466; text-align:center;}
button[kind="secondary"] {background:#6b4a26 !important; border:2px solid #b8924a !important; color:#ffe9a8 !important;}
</style>
""", unsafe_allow_html=True)

st.title("⚔️ 스탯 찍기 게임")
st.caption("※ 학습용 가상 캐릭터 데이터(60명)입니다. 전투력은 STR, INT, WIS, CON, DEX 다섯 스탯으로 정해집니다.")

# ===== Step 1. 데이터 준비 =====
데이터 = pd.read_csv("캐릭터_스탯.csv")
스탯이름 = ["STR", "INT", "WIS", "CON", "DEX"]
아이콘 = ["💪", "🧠", "🔮", "🛡️", "💨"]

with st.expander("📋 캐릭터 데이터 보기 (60명)"):
    st.dataframe(데이터)

# ===== 사이드바: 설정 =====
st.sidebar.header("⚙️ 설정")
시험용_비율 = st.sidebar.slider("시험용 데이터 비율", 0.1, 0.5, 0.2, 0.05)
시드 = st.sidebar.number_input("random_state (섞는 번호)", min_value=0, max_value=100, value=2)

# --- 직접 작성 시작 (Step 2: 나누기) ---
X = 데이터[["STR", "INT", "WIS", "CON", "DEX"]]
y = 데이터["전투력"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=시험용_비율, random_state=시드)
# --- 직접 작성 끝 ---

# --- 직접 작성 시작 (Step 3: 학습) ---
모델 = LinearRegression()
모델.fit(X_train, y_train)
# --- 직접 작성 끝 ---

# --- 직접 작성 시작 (Step 4: 점수 계산) ---
train_예측 = 모델.predict(X_train)
test_예측 = 모델.predict(X_test)
공부용_MSE = mean_squared_error(y_train, train_예측)
시험용_MSE = mean_squared_error(y_test, test_예측)
시험용_MAE = mean_absolute_error(y_test, test_예측)
# --- 직접 작성 끝 ---

# --- 직접 작성 시작 (Step 5: 기준선 만들기) ---
평균전투력 = y_train.mean()
기준선_예측 = [평균전투력] * len(y_test)
기준선_MSE = mean_squared_error(y_test, 기준선_예측)
# --- 직접 작성 끝 ---

# --- 직접 작성 시작 (Step 6: 입력 늘려 보기) ---
점수표_이름 = ["평균만 찍기"]
점수표_값 = [기준선_MSE]
입력들 = [["STR"], ["STR", "DEX"], ["STR", "DEX", "CON"], ["STR", "INT", "WIS", "CON", "DEX"]]
for 입력 in 입력들:
    작은모델 = LinearRegression()
    작은모델.fit(X_train[입력], y_train)
    작은예측 = 작은모델.predict(X_test[입력])
    점수표_이름.append(" + ".join(입력))
    점수표_값.append(mean_squared_error(y_test, 작은예측))
# --- 직접 작성 끝 ---

# ===== 화면 =====
탭1, 탭2, 탭3 = st.tabs(["🎲 전투력 맞히기", "📜 스탯 창 · 최강 빌드", "📊 입력을 늘리면?"])

# ---------- 탭 1: 전투력 맞히기 (사람 vs AI) ----------
with 탭1:
    st.subheader("🎲 전투력 맞히기: 나 vs AI")
    st.write("스탯만 보고 전투력을 맞혀 보세요. 5명을 맞히면 **내 평균 오차(MAE)** 와 **AI의 평균 오차**를 비교합니다.")

    if "게임_스탯" not in st.session_state:
        st.session_state["게임_스탯"] = []
        st.session_state["게임_정답"] = []
        st.session_state["내_답"] = []

    if st.button("🎮 새 게임 시작 (시험용 캐릭터 5명)"):
        번호들 = random.sample(range(len(X_test)), 5)
        st.session_state["게임_스탯"] = X_test.iloc[번호들].values.tolist()
        st.session_state["게임_정답"] = y_test.iloc[번호들].tolist()
        st.session_state["내_답"] = []

    스탯들 = st.session_state["게임_스탯"]
    정답들 = st.session_state["게임_정답"]
    내답들 = st.session_state["내_답"]

    if len(스탯들) == 0:
        st.info("위 버튼을 눌러 게임을 시작하세요.")
    elif len(내답들) < 5:
        지금 = len(내답들)
        st.write(f"**{지금 + 1}번째 캐릭터** (5명 중)")
        칸들 = st.columns(5)
        for 칸, 이름, 이모지, 값 in zip(칸들, 스탯이름, 아이콘, 스탯들[지금]):
            칸.metric(f"{이모지} {이름}", int(값))
        내_추측 = st.number_input("내가 예상하는 전투력", min_value=0, max_value=100, value=30, key=f"guess_{지금}")
        if st.button("제출", key=f"submit_{지금}"):
            st.session_state["내_답"].append(내_추측)
            st.rerun()
    else:
        AI예측 = 모델.predict(pd.DataFrame(스탯들, columns=스탯이름))
        표 = pd.DataFrame({
            "정답": 정답들,
            "내 답": 내답들,
            "AI 예측": [round(v) for v in AI예측],
        }, index=range(1, 6))
        표["내가 틀린 크기"] = (표["정답"] - 표["내 답"]).abs()
        표["AI가 틀린 크기"] = (표["정답"] - 표["AI 예측"]).abs()
        st.dataframe(표)
        내_MAE = 표["내가 틀린 크기"].mean()
        AI_MAE = 표["AI가 틀린 크기"].mean()
        칸1, 칸2 = st.columns(2)
        칸1.metric("내 MAE", f"{내_MAE:.1f}")
        칸2.metric("AI의 MAE", f"{AI_MAE:.1f}")
        if AI_MAE < 내_MAE:
            st.success("이번엔 AI가 더 정확했어요! 스탯 5개를 동시에 계산하는 건 사람에게 어렵죠.")
        else:
            st.info("이번엔 사람이 이겼어요! 5번은 적은 횟수라 운이 섞여요.")

# ---------- 탭 2: 스탯 창 · 최강 빌드 ----------
with 탭2:
    st.subheader("📜 스탯 포인트 10개로 최강 빌드를 만들어 보세요")
    for 이름 in 스탯이름:
        if 이름 not in st.session_state:
            st.session_state[이름] = 3
    if "남은" not in st.session_state:
        st.session_state["남은"] = 10

    def 올리기(이름):
        if st.session_state["남은"] > 0:
            st.session_state[이름] += 1
            st.session_state["남은"] -= 1

    def 초기화():
        for 이름 in 스탯이름:
            st.session_state[이름] = 3
        st.session_state["남은"] = 10

    좌, 우 = st.columns(2)
    with 좌:
        with st.container(border=True):
            st.markdown("**📜 스탯 창**")
            for 이름, 이모지 in zip(스탯이름, 아이콘):
                a, b, c = st.columns([2, 1.3, 1])
                a.markdown(f"<span class='stat'>{이모지} {이름}</span>", unsafe_allow_html=True)
                b.markdown(f"<span class='val'>{st.session_state[이름]}</span>", unsafe_allow_html=True)
                c.button("▲", key="up_" + 이름, on_click=올리기, args=(이름,))
            st.markdown(f"남은 포인트: **{st.session_state['남은']}**")
            st.button("초기화", on_click=초기화)

    현재 = [st.session_state[이름] for 이름 in 스탯이름]
    예측전투력 = 모델.predict(pd.DataFrame([현재], columns=스탯이름))[0]
    쓴포인트 = 10 - st.session_state["남은"]
    후광 = max(0, int((예측전투력 - 18) // 6))
    hp = 100 + st.session_state["CON"] * 10
    mp = 20 + st.session_state["INT"] * 8 + st.session_state["WIS"] * 4

    with 우:
        if os.path.exists("내_캐릭터.png"):
            st.image("내_캐릭터.png")   # 선생님이 준비한 이미지가 있으면 그걸 보여 줍니다
        else:
            st.markdown(장면_svg("용사", 1 + 쓴포인트, 후광), unsafe_allow_html=True)
        st.markdown(f"**HP** {hp}")
        st.markdown(f"<div class='bar'><div class='hp' style='width:{min(hp / 250 * 100, 100)}%'></div></div>", unsafe_allow_html=True)
        st.markdown(f"**MP** {mp}")
        st.markdown(f"<div class='bar'><div class='mp' style='width:{min(mp / 250 * 100, 100)}%'></div></div>", unsafe_allow_html=True)
        st.markdown("**🤖 AI가 예측한 전투력**")
        st.markdown(f"<div class='big'>{예측전투력:.0f}</div>", unsafe_allow_html=True)

    with st.expander("🔎 AI가 알아낸 스탯 효율 (스탯을 1 올리면 전투력이 얼마나 오르나)"):
        효율표 = pd.DataFrame({"스탯": 스탯이름, "스탯 1 올리면": [round(w, 2) for w in 모델.coef_]})
        st.dataframe(효율표, hide_index=True)
        st.caption("숫자가 클수록 효율이 좋은 스탯입니다. 0에 가까우면 전투력에 거의 영향이 없는 스탯이에요.")

    with st.expander("🏆 포인트 10개를 한 스탯에 몰아 찍으면?"):
        몰빵값 = []
        for 번호 in range(5):
            빌드 = [3, 3, 3, 3, 3]
            빌드[번호] += 10
            몰빵값.append(round(모델.predict(pd.DataFrame([빌드], columns=스탯이름))[0]))
        st.dataframe(pd.DataFrame({"몰아준 스탯": 스탯이름, "예측 전투력": 몰빵값}), hide_index=True)

# ---------- 탭 3: 입력을 늘리면? ----------
with 탭3:
    st.subheader("📊 입력(스탯)을 늘리면 점수가 어떻게 달라질까?")
    st.write("시험용 MSE입니다. **낮을수록 좋은 모델**이에요.")
    결과표 = pd.DataFrame({"입력": 점수표_이름, "시험용 MSE": [round(v, 1) for v in 점수표_값]})
    st.dataframe(결과표, hide_index=True)
    st.bar_chart(결과표, x="입력", y="시험용 MSE", sort=False)
    칸1, 칸2, 칸3 = st.columns(3)
    칸1.metric("공부용 MSE (5개 전부)", f"{공부용_MSE:.1f}")
    칸2.metric("시험용 MSE (5개 전부)", f"{시험용_MSE:.1f}")
    칸3.metric("시험용 MAE (5개 전부)", f"{시험용_MAE:.1f}")
    st.info("👉 STR만, STR+DEX, STR+DEX+CON으로 입력을 늘릴수록 점수가 크게 줄어듭니다. "
            "그런데 INT, WIS까지 넣은 5개 전부는 더 좋아졌나요? 직접 확인해 보세요.")
