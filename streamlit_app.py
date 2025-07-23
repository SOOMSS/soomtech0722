import streamlit as st
import io
from datetime import datetime

st.set_page_config(page_title="🏡 Minecraft 주택설계 시뮬레이터", layout="wide")
st.title("🏡 Minecraft 주택설계 시뮬레이터")
st.markdown("""
Minecraft에서 집 짓기 전에 아이디어를 설계하고, 블록 수를 계산하며,
블럭코딩 예시까지 제공하는 통합 설계 시뮬레이터입니다.
""")
st.markdown("---")

# 초기 세션 상태 설정
def init_session():
    keys = ["house_type", "rooms", "baths", "kitchen", "storage", "location", "materials", 
            "highlight", "room_styles", "submitted"]
    for key in keys:
        if key not in st.session_state:
            st.session_state[key] = None if key != "materials" and key != "room_styles" else [] if key == "materials" else {}

init_session()

st.header("1️⃣ 주택 형태 선택")
house_type = st.selectbox("주택 구조를 선택하세요", ["단층", "복층", "ㄱ자형", "ㄷ자형", "L자형", "자유형"])
st.session_state.house_type = house_type

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

st.header("3️⃣ 위치 및 자재 선택")
st.session_state.location = st.selectbox("집을 지을 장소는 어디인가요?", ["바닷가", "산 근처", "숲속", "도시 중심", "들판", "자유"])
st.session_state.materials = st.multiselect(
    "사용할 마인크래프트 블록을 선택하세요:",
    ["Oak Planks", "Stone Bricks", "Glass Pane", "Brick Block", "Concrete", "Iron Block"]
)

st.header("4️⃣ 방별 스타일 지정")
st.session_state.room_styles = {}
for i in range(1, st.session_state.rooms + 1):
    room_name = f"방 {i}"
    style = st.selectbox(f"{room_name} 용도 선택:", ["침실", "공부방", "작업실", "게임방", "게스트룸", "기타"], key=f"room_{i}")
    st.session_state.room_styles[room_name] = style

st.session_state.highlight = st.text_input("강조하고 싶은 공간 (예: 통유리 거실, 옥상 정원 등)")

st.markdown("---")

col_submit, col_calc, col_detail = st.columns([1, 1, 1])
with col_submit:
    if st.button("📋 설계안 보기"):
        st.session_state.submitted = True

with col_calc:
    block_calc_clicked = st.button("🧱 블럭 구조 계산기")

with col_detail:
    if st.button("🏠 방 1 세부설정하기"):
        st.markdown("""
        <meta http-equiv="refresh" content="0;url=./room1" />
        """, unsafe_allow_html=True)

if st.session_state.submitted:
    st.subheader("📋 나의 주택 설계 보고서")
    st.markdown(f"""
    **설계 개요**  
    위치: **{st.session_state.location}**, 구조: **{st.session_state.house_type}**, 
    방: **{st.session_state.rooms}개**, 욕실: **{st.session_state.baths}개**, 
    주방: **{st.session_state.kitchen}**, 창고: **{st.session_state.storage}**  
    사용 블록: **{', '.join(st.session_state.materials)}**  
    강조 공간: **{st.session_state.highlight or '없음'}""")

    st.markdown("**방별 스타일:**")
    for room, style in st.session_state.room_styles.items():
        st.markdown(f"- {room}: {style}")

    st.markdown("---")

    if block_calc_clicked:
        block_per_room = 5 * 5 * 3
        block_per_bath = 3 * 3 * 3
        block_kitchen = 5 * 3 * 3 if st.session_state.kitchen == "예" else 0
        block_storage = 3 * 3 * 3 if st.session_state.storage == "예" else 0
        block_total = st.session_state.rooms * block_per_room + st.session_state.baths * block_per_bath + block_kitchen + block_storage

        st.subheader("📦 예상 블록 수 계산 결과")
        st.write(f"총 예상 블록 수: **{block_total} 개**")

        st.subheader("💡 블럭코딩 구조 예시")
        base_material = st.session_state.materials[0] if st.session_state.materials else "stone"

        code_example = f"""
# 예시: Minecraft에서 집 짓기 (Python 블럭코딩 기반)
player_pos = positions.get_player_world_position()

# 바닥 만들기
blocks.fill(BLOCKS.{base_material.upper().replace(' ', '_')},
            world(0, 0, 0),
            world({5*st.session_state.rooms}, 0, {5*st.session_state.baths}))

# 벽 세우기
blocks.fill(BLOCKS.{base_material.upper().replace(' ', '_')},
            world(0, 1, 0),
            world({5*st.session_state.rooms}, 3, 0))
blocks.fill(BLOCKS.{base_material.upper().replace(' ', '_')},
            world(0, 1, {5*st.session_state.baths}),
            world({5*st.session_state.rooms}, 3, {5*st.session_state.baths}))

# 천장
blocks.fill(BLOCKS.{base_material.upper().replace(' ', '_')},
            world(0, 4, 0),
            world({5*st.session_state.rooms}, 4, {5*st.session_state.baths}))
"""
        st.code(code_example, language="python")
        st.info("학생들은 이 코드를 참고하여 구조물을 자동으로 생성하거나, MakeCode 블럭으로 직접 조립할 수 있습니다.")
