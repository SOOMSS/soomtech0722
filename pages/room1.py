import streamlit as st

st.set_page_config(page_title="🛋️ 방 세부 설정", layout="centered")
st.title("🛋️ 방별 세부 스타일 설정")

def init_room_session():
    defaults = {
        "current_room": 1,
        "rooms": 1,
        "room_details": {},
        "house_type": "단층",
        "materials": ["Oak Planks"],
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_room_session()

room_index = st.session_state.current_room
room_name = f"방 {room_index}"

st.header(f"{room_name} 세부 설정")

# 선택 항목
color = st.selectbox("벽 색상", ["화이트", "블루", "라이트 그레이", "옐로우", "우드톤"])
floor = st.selectbox("바닥 재질", ["나무", "돌", "카펫", "콘크리트"])
light = st.selectbox("조명 종류", ["램프", "천장등", "촛불", "Glowstone"])
furniture = st.multiselect("주요 가구 선택", ["침대", "책상", "옷장", "소파", "컴퓨터 책상", "TV", "책장"])

# 설정 저장
if st.button("✅ 설정 저장"):
    st.session_state.room_details[room_name] = {
        "벽 색상": color,
        "바닥 재질": floor,
        "조명": light,
        "가구": furniture
    }
    st.success(f"{room_name}의 세부 설정이 저장되었습니다!")

# 다음 방 이동 or 완료
if room_index < st.session_state.rooms:
    if st.button("➡️ 다음 방으로 이동"):
        st.session_state.current_room += 1
        st.experimental_rerun()
else:
    st.markdown("✅ 모든 방의 설정이 완료되었습니다!")
    if st.button("🏠 메인 페이지로 돌아가기"):
        st.session_state.current_room = 1
        st.switch_page("streamlit_app.py")
