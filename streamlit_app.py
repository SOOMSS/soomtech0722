import streamlit as st
import os

st.set_page_config(page_title="🏡 Minecraft 주택설계 시뮬레이터", layout="centered")
st.markdown("<h1 style='text-align:center;color:#4CAF50;'>🏡 Minecraft 주택설계 시뮬레이터</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Minecraft에서 집 짓기 전에 아이디어를 정리해보세요!</p>", unsafe_allow_html=True)
st.markdown("---")

# 초기 세션 상태 설정
def init_session():
    keys = ["house_type", "rooms", "baths", "kitchen", "storage", "location", "materials", "highlight", "submitted", "room_styles", "go_to_room_detail", "current_room", "room_details"]
    for key in keys:
        if key not in st.session_state:
            if key == "materials":
                st.session_state[key] = []
            elif key == "room_styles" or key == "room_details":
                st.session_state[key] = {}
            elif key == "go_to_room_detail":
                st.session_state[key] = False
            elif key == "submitted":
                st.session_state[key] = False
            elif key == "current_room":
                st.session_state[key] = 1
            else:
                st.session_state[key] = None

init_session()

st.header("1️⃣ 주택 형태 선택")
house_type = st.selectbox("주택 구조를 선택하세요", ["단층", "복층", "ㄱ자형", "ㄷ자형", "L자형", "자유형"])
st.session_state.house_type = house_type

# 구조별 방/화장실 제한 설정
structure_options = {
    "단층": {"rooms": [1, 2, 3], "baths": [1, 2]},
    "복층": {"rooms": [2, 3, 4, 5], "baths": [2, 3]},
    "ㄱ자형": {"rooms": [2, 3, 4], "baths": [1, 2]},
    "ㄷ자형": {"rooms": [3, 4, 5], "baths": [2, 3]},
    "L자형": {"rooms": [2, 3], "baths": [1, 2]},
    "자유형": {"rooms": [1, 2, 3, 4, 5], "baths": [1, 2, 3]},
}

st.header("2️⃣ 공간 구성 선택")
st.session_state.rooms = st.radio("방 개수", structure_options[house_type]["rooms"], horizontal=True)
st.session_state.baths = st.radio("화장실 개수", structure_options[house_type]["baths"], horizontal=True)
st.session_state.kitchen = st.radio("주방 포함 여부", ["예", "아니오"], horizontal=True)
st.session_state.storage = st.radio("창고 포함 여부", ["예", "아니오"], horizontal=True)

st.header("3️⃣ 위치 환경 선택")
st.session_state.location = st.selectbox("집을 지을 장소는 어디인가요?", ["바닷가", "산 근처", "숲속", "도시 중심", "들판", "자유"])

st.header("4️⃣ 마인크래프트 블록 자재 선택")
st.session_state.materials = st.multiselect(
    "사용할 마인크래프트 블록을 선택하세요:",
    ["Oak Planks", "Stone Bricks", "Glass Pane", "Brick Block", "Concrete", "Iron Block"]
)

st.header("5️⃣ 강조하고 싶은 공간")
st.session_state.highlight = st.text_input("예: 통유리 거실, 옥상 정원 등")

st.header("6️⃣ 방별 스타일 지정")
st.session_state.room_styles = {}
for i in range(1, st.session_state.rooms + 1):
    room_name = f"방 {i}"
    style = st.selectbox(f"{room_name} 용도 선택:", ["침실", "공부방", "작업실", "게임방", "게스트룸", "기타"], key=f"room_{i}")
    st.session_state.room_styles[room_name] = style

# 버튼 배치
col1, col2 = st.columns(2)
with col1:
    if st.button("🏗️ 설계안 보기"):
        st.session_state.submitted = True
        st.session_state.go_to_room_detail = True
with col2:
    if st.button("🔄 초기화"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

# 설계안 출력
if st.session_state.submitted:
    st.subheader("📋 나의 주택 설계 보고서")
    st.markdown(f"""
    **1. 설계 개요**  
    이 설계는 **{st.session_state.location}**에 건축될 **{st.session_state.house_type}** 구조의 주택입니다.  
    주거의 실용성과 주변 환경과의 조화를 고려하여 공간과 자재를 선정하였습니다.

    **2. 공간 구성**  
    방은 **{st.session_state.rooms}개**, 욕실은 **{st.session_state.baths}개**로 가족 단위의 생활을 고려했습니다.  
    주방: **{st.session_state.kitchen}**, 창고: **{st.session_state.storage}**

    **3. 방별 스타일**  
    """)
    for room, style in st.session_state.room_styles.items():
        st.markdown(f"- {room}: {style}")

    st.markdown(f"""
    **4. 자재 및 강조**  
    자재: **{', '.join(st.session_state.materials)}**  
    강조 공간: **{st.session_state.highlight if st.session_state.highlight else '없음'}**
    """)

    if st.button("🏠 방 1 세부설정하기"):
        st.switch_page = lambda page: st.markdown(f'<meta http-equiv="refresh" content="0;url=./{page}">', unsafe_allow_html=True)
        st.switch_page("room1")
