import streamlit as st
import pandas as pd
import openai

# 페이지 설정
st.set_page_config(
    page_title="건축양식 정보",
    page_icon="\ud3ec\ud0c4\ud30c\uc774",
    layout="wide"
)

# CSS 스타일링
st.markdown("""
<style>
    .info-header {
        background: linear-gradient(90deg, #059669, #047857);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 사이드바: OpenAI API 키 입력 ---
with st.sidebar:
    st.markdown("### \ud83d\udd10 OpenAI API \ud0a4 \uc785\ub825")
    user_api_key = st.text_input(
        "OpenAI API \ud0a4\ub97c \uc785\ub825\ud558\uc138\uc694 (\uc608: sk-...)",
        type="password",
        placeholder="sk-\ub85c \uc2dc\uc791\ud558\ub294 \ud0a4 \uc785\ub825"
    )

    if user_api_key:
        try:
            openai.api_key = user_api_key
            openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            st.success("\u2705 API \ud0a4\uac00 \uc720\ud6a8\ud569\ub2c8\ub2e4.")
            st.session_state.api_valid = True
            st.session_state.user_api_key = user_api_key
        except Exception as e:
            st.error("\u274c API \ud0a4 \uc624\ub958: \uc720\ud6a8\ud558\uc9c0 \uc54a\uac70\ub098 \uc0ac\uc6a9 \uc81c\ud55c\ub429\ub2c8\ub2e4")
            st.session_state.api_valid = False

    st.markdown("### \ud83c\udf1f \ud559\uc2b5 \ubaa9\ud45c")
    st.info("""
    **이 페이지에서 학습할 내용:**
    - 세계 각국의 건축양식 특징
    - 기후가 건축에 미치는 영향
    - 지역별 건축 재료와 기법
    - 설계 시 고려해야 할 요소들
    """)

    if st.session_state.get("selected_country") and st.session_state.get("selected_city"):
        st.markdown("### \ud83d\udcca 현재 선택 정보")
        st.write(f"**국가**: {st.session_state.selected_country}")
        st.write(f"**도시**: {st.session_state.selected_city}")

        climate = {
            "avg_temp": "15.0°C",
            "humidity": "70%"
        }  # 간이 예시, 실제 데이터 연결 필요

        temp = float(climate['avg_temp'].replace('°C', ''))
        humidity = int(climate['humidity'].replace('%', ''))

        chart_data = pd.DataFrame({
            '기온(°C)': [temp],
            '습도(%)': [humidity]
        })

        st.markdown(f"#### \ud83c\udf21️ {st.session_state.selected_city} 기후 지표 시각화")
        st.bar_chart(chart_data)

    st.markdown("### \ud83d\udca1 설계 팁")
    st.warning("""
    **좋은 건축 설계를 위해:**
    1. 지역 기후를 충분히 분석하세요
    2. 전통 건축의 지혜를 활용하세요  
    3. 현지 재료를 우선 고려하세요
    4. 지속가능성을 염두에 두세요
    """)

# --- GPT 요약 함수 ---
def get_gpt_summary(prompt_text, api_key):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 건축 전문가입니다."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT 호출 실패: {e}"

# --- 건축 데이터 예시 ---
architecture_data = {
    "일본": {
        "도시": ["도쿄", "교토"]
    },
    "한국": {
        "도시": ["서울", "부산"]
    }
}

# --- 국가 / 도시 선택 ---
st.markdown('<div class="info-header"><h1>🏛️ 세계 건축양식 정보</h1></div>', unsafe_allow_html=True)

country = st.selectbox("🌍 국가 선택", ["선택하세요"] + list(architecture_data.keys()))
if country != "선택하세요":
    city = st.selectbox("🏙️ 도시 선택", ["선택하세요"] + architecture_data[country]["도시"])
else:
    city = None

# 선택 정보 저장
if country != "선택하세요":
    st.session_state.selected_country = country
if city and city != "선택하세요":
    st.session_state.selected_city = city

# --- GPT 요약 표시 ---
if (
    st.session_state.get("api_valid")
    and st.session_state.get("user_api_key")
    and st.session_state.get("selected_country")
    and st.session_state.get("selected_city")
):
    st.markdown("## 🤖 GPT 건축 요약 설명")

    prompt = f"{st.session_state.selected_country} {st.session_state.selected_city}의 전통 및 현대 건축 양식과 기후 적응 특징을 요약해줘."

    with st.spinner("ChatGPT에게 건축 요약을 요청 중..."):
        gpt_result = get_gpt_summary(prompt, st.session_state["user_api_key"])

    st.markdown(gpt_result)
