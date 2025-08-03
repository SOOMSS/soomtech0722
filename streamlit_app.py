import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="SOOMTECH Minecraft EDU",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
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

    .course-info {
        background: #fef3c7;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #f59e0b;
        margin: 2rem 0;
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

# 헤더 배너
st.markdown("""
<div class="main-header">
    <div class="main-header-content">
        <h1>📘 마인크래프트 건축 수업</h1>
        <p>도면을 보고 상상하고, 설계하고, 구현하기</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown("### ⚙️ 설정")
    api_key = st.text_input("API Key", type="password", placeholder="API 키를 입력하세요")
    
    st.markdown("### 📚 수업 정보")
    st.info("""
    **수업 주제**: 마인크래프트 건축 시뮬레이션  
    **대상**: 중학교 2학년  
    **교과**: 기술  
    **차시**: 8차시
    """)

# 수업 소개
st.markdown("### 📖 수업 소개")
st.markdown("이 웹앱은 중학교 2학년 기술 수업을 위한 창의적이고 혁신적인 학습 도구입니다.  \n도면 읽기부터 3D 건축물 설계까지 다양한 활동을 통해 **공간지각능력**과 **창의성**을 기를 수 있습니다.")

# 학습 메뉴
st.markdown("## 🎯 학습 메뉴")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🧱</div>
        <h3>정투상법</h3>
        <p>도면 기반 퀴즈</p>
        <small>정면도, 평면도, 우측면도 퀴즈</small>
    </div>
    """, unsafe_allow_html=True)
    if st.button("정투상법 시작", key="orthographic", use_container_width=True):
        st.session_state.selected_menu = "정투상법"

with col2:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🖥️</div>
        <h3>설계사무실</h3>
        <p>나라/ 도시 선택</p>
        <small>건축양식 및 나라 특징 알아보기</small>
    </div>
    """, unsafe_allow_html=True)
    if st.button("일반모드 시작", key="general", use_container_width=True):
        st.session_state.selected_menu = "일반모드"

with col3:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">🏛️</div>
        <h3>설계사무실</h3>
        <p>가상 건축 설계</p>
        <small>창의적 건축물 설계</small>
    </div>
    """, unsafe_allow_html=True)
    if st.button("설계사무실 시작", key="design", use_container_width=True):
        st.session_state.selected_menu = "설계사무실"

with col4:
    st.markdown("""
    <div class="menu-card">
        <div class="menu-icon">💻</div>
        <h3>블록코딩</h3>
        <p>Minecraft 연동</p>
        <small>Minecraft EDU와 연동된 코딩</small>
    </div>
    """, unsafe_allow_html=True)
    if st.button("블록코딩 시작", key="coding", use_container_width=True):
        st.session_state.selected_menu = "블록코딩"

# 수업 목표
st.markdown("""
<div class="objectives-section">
    <h3 style="text-align: center; margin-bottom: 1rem;">🎯 수업 목표 및 활동</h3>
    <div style="display: flex; flex-direction: column; align-items: center; font-size: 1.1rem; line-height: 1.8;">
        <div style="text-align: left; width: 80%;">
            1. 도면(정면도, 평면도, 우측면도 등)을 기반으로 입체 구조를 시각적으로 유추할 수 있다.<br>
            2. 선택한 국가와 도시의 건축양식, 기후, 랜드마크의 정보를 분석하여 설계에 반영할 수 있다.<br>
            3. 자신만의 설계를 Minecraft EDU를 활용하여 건축할 수 있다.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



# 수업 역량
st.markdown("""
<div class="course-info">
    <h4>📋 관련 역량 및 성취기준</h4>
    <ul>
        <li><strong>기술적 문제 해결 역량</strong> - 도면 읽기와 공간 지각</li>
        <li><strong>기술 시스템 이해</strong> - 건축 시스템의 구조와 원리</li>
        <li><strong>의사소통 및 협업 능력</strong> - 팀 프로젝트를 통한 협업</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 차시별 계획
with st.expander("📅 차시별 수업 계획 보기"):
    st.markdown("""
    | 차시 | 수업 내용 |
    |------|-----------|
    | 1차시 | 건축의 기능 및 공간적 요소 탐색 |
    | 2차시 | 입체도형 추론 퀴즈 및 도시별 양식 탐색 |
    | 3차시 | 가상 건축물 설계 |
    | 4~7차시 | Minecraft EDU 구현 |
    | 8차시 | 발표 및 평가 |
    """)

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; font-size: 0.9rem;">
    <p>🏫 중학교 2학년 기술 수업 | 👥 8차시 프로그램 | 🎯 창의성과 문제해결능력 향상</p>
</div>
""", unsafe_allow_html=True)
