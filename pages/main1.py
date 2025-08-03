import streamlit as st
import openai

# 페이지 기본 설정
st.set_page_config(
    page_title="SOOMTECH Minecraft EDU",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 상태 초기화
if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = None

# --- CSS 스타일링 ---
st.markdown("""
<style>
    .main-header {
        position: relative;
        color: white;
        text-align: center;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 2rem;
        height: 250px;
    }

    .main-header::before {
        content: "";
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), 
                    url("https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130329_299%2Fkgk3377_13645414165827r1hD_PNG%2F2013-03-28_20.00.52.png&type=l340_165");
        background-size: cover;
        background-position: center;
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: 0;
    }

    .main-header-content {
        position: relative;
        z-index: 1;
        background-color: rgba(0, 0, 0, 0.6);
        display: inline-block;
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-top: 50px;
    }

    .menu-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 3px solid #fbbf24;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .menu-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .menu-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .objectives-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 3px solid #fbbf24;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- 헤더 배너 ---
st.markdown("""
<div class="main-header">
    <div class="main-header-content">
        <h1>📘 마인크래프트 건축 수업</h1>
        <p>도면을 보고 상상하고, 설계하고, 구현하기</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 사이드바 ---
with st.sidebar:
    st.markdown("### ⚙️ 설정")
    api_key = st.text_input("🔐 GPT API Key", type="password", placeholder="OpenAI API 키를 입력하세요")

    st.markdown("### 📚 수업 정보")
    st.info("""
    **수업 주제**: 마인크래프트 건축 시뮬레이션  
    **대상**: 중학교 2학년  
    **교과**: 기술  
    **차시**: 8차시
    """)

    st.markdown("---")
    st.markdown("### 🧭 학습 메뉴")
    selected = st.selectbox(
        "학습 모드를 선택하세요",
        ("홈", "정투상법", "일반모드", "설계사무실", "블록코딩"),
    )
    st.session_state.selected_menu = selected

# --- 메인 콘텐츠 ---
if st.session_state.selected_menu == "홈":
    st.markdown("## 🎯 학습 메뉴")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-icon">🧱</div>
            <h3>정투상법</h3>
            <p>도면 기반 퀴즈</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-icon">🗺️</div>
            <h3>일반모드</h3>
            <p>도시 선택 → 건축양식 정보</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-icon">🏛️</div>
            <h3>설계사무실</h3>
            <p>건축 도면 설계</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-icon">💻</div>
            <h3>블록코딩</h3>
            <p>Minecraft 연동</p>
        </div>
        """, unsafe_allow_html=True)

# --- 일반모드: 도시 선택 + GPT 연동 ---
elif st.session_state.selected_menu == "일반모드":
    st.subheader("🗺️ 도시 선택 후 건축양식 정보 보기")

    country_city_map = {
        "대한민국": ["서울", "부산", "경주"],
        "일본": ["도쿄", "오사카", "쿄토"],
        "프랑스": ["파리", "리옹", "니스"],
        "이탈리아": ["로마", "피렌체", "밀라노"]
    }

    country = st.selectbox("🌍 국가를 선택하세요", list(country_city_map.keys()))
    city = st.selectbox("🏙️ 도시를 선택하세요", country_city_map[country])

    if st.button("🔎 정보 확인하기") and api_key:
        with st.spinner(f"🔄 {city}의 정보를 불러오는 중입니다..."):
            prompt = f"""
            {country} {city}의 건축 양식, 기후 특징, 유명한 랜드마크에 대해 간단하고 명확하게 정리해줘.
            1. 건축양식 (예시 스타일 포함)
            2. 기후 특징 (연평균 온도 등)
            3. 주요 랜드마크 (3개 정도)
            """
            try:
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                answer = response["choices"][0]["message"]["content"]
                st.markdown("### 📖 검색 결과")
                st.success(answer)
            except Exception as e:
                st.error(f"오류 발생: {e}")
    else:
        st.info("API 키를 입력하고 '정보 확인하기' 버튼을 눌러주세요.")

# --- 정투상법, 설계사무실, 블록코딩은 추후 구현 예정 ---
else:
    st.markdown("🚧 현재 선택한 메뉴는 아직 준비 중입니다.")
