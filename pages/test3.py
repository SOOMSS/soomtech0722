import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="건축 설계 도구", layout="wide")

st.title("🏗️ 마인크래프트 건축 설계 도구")
st.markdown("""
좌측에서 건축양식을 선택하고,
중앙 도면 캔버스에 직접 설계를 그려보세요!
도면은 저장하거나 다운로드할 수 있습니다.
""")

# 색상 선택
stroke_color = st.color_picker("선 색상 선택", "#000000")

# 도구 선택
mode = st.radio(
    "도구 모드 선택",
    ("freedraw", "line", "rect", "circle", "transform"),
    index=0,
    horizontal=True
)

# 캔버스
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.0)",  # 채우기 색 없음
    stroke_width=3,
    stroke_color=stroke_color,
    background_color="#ffffff",
    update_streamlit=True,
    height=500,
    width=800,
    drawing_mode=mode,
    key="canvas"
)

# 이미지 저장하기
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
    with st.expander("💾 도면 이미지 다운로드"):
        st.download_button(
            label="🖼️ PNG로 저장",
            data=canvas_result.image_data,
            file_name="architecture_drawing.png",
            mime="image/png"
        )
