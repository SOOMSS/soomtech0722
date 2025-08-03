import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="정투상법 퀴즈",
    page_icon="📐",
    layout="wide"
)

# CSS 스타일링
st.markdown("""
<style>
    .quiz-header {
        background: linear-gradient(90deg, #d97706, #ea580c);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .drawing-card {
        background: #fef3c7;
        border: 3px solid #d97706;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .drawing-title {
        background: #d97706;
        color: white;
        padding: 0.5rem;
        border-radius: 8px;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .shape-display {
        font-size: 8rem;
        margin: 1rem 0;
    }
    
    .answer-card {
        background: #1e40af;
        border: 3px solid #1d4ed8;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .answer-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .answer-selected {
        background: #059669 !important;
        border-color: #047857 !important;
    }
    
    .answer-correct {
        background: #16a34a !important;
        border-color: #15803d !important;
    }
    
    .answer-wrong {
        background: #dc2626 !important;
        border-color: #b91c1c !important;
    }
    
    .score-display {
        background: #fbbf24;
        color: #92400e;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

import streamlit as st

# 1번 문제 데이터
quiz = {
    "id": 1,
    "description": "정육면체",
    "front_view_img": "https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8942.jpg?raw=true",
    "top_view_img": "https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8943.jpg?raw=true",
    "right_view_img": "https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8944.jpg?raw=true",
    "options_img": [
        "https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8946.jpg?raw=true",  # 정답
        "https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8947.jpg?raw=true",  # 오답
        "https://github.com/SOOMSS/minecraft_picture/blob/main/IMG_8948.jpg?raw=true"   # 오답
    ],
    "correct_answer_index": 0
}

# 문제 정보 출력
st.markdown(f"### 🧠 문제 {quiz['id']} - {quiz['description']}")

# 3면도 이미지 출력: 가로 정렬
st.markdown("#### 🖼️ 3면도 보기")
view_cols = st.columns(3)
with view_cols[0]:
    st.image(quiz["front_view_img"], caption="정면도", width=200)
with view_cols[1]:
    st.image(quiz["top_view_img"], caption="평면도", width=200)
with view_cols[2]:
    st.image(quiz["right_view_img"], caption="우측면도", width=200)

# 보기 이미지 출력 + 선택 버튼
st.markdown("#### ❓ 어떤 입체 구조일까요?")
option_cols = st.columns(len(quiz["options_img"]))
selected_option = None

for idx, (col, img_url) in enumerate(zip(option_cols, quiz["options_img"])):
    with col:
        st.image(img_url, caption=f"선택 {idx + 1}", width=150)
        if st.button(f"선택 {idx + 1}", key=f"option_{idx}"):
            selected_option = idx

# 정답 확인
if selected_option is not None:
    if selected_option == quiz["correct_answer_index"]:
        st.success("✅ 정답입니다! 잘했어요.")
    else:
        st.error("❌ 오답입니다. 다시 생각해보세요.")


# 세션 상태 초기화
if 'quiz_initialized' not in st.session_state:
    st.session_state.quiz_initialized = True
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.quiz_questions = random.sample(quiz_data, len(quiz_data))

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.quiz_questions = random.sample(quiz_data, len(quiz_data))

def next_question():
    if st.session_state.current_question < len(st.session_state.quiz_questions) - 1:
        st.session_state.current_question += 1
        st.session_state.answered = False
        st.session_state.selected_answer = None
    else:
        st.session_state.quiz_completed = True

# 메인 헤더
st.markdown("""
<div class="quiz-header">
    <h1>📐 정투상법 퀴즈</h1>
    <p>3면도를 보고 올바른 입체도형을 선택하세요!</p>
</div>
""", unsafe_allow_html=True)

# 네비게이션 버튼들
col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
with col_nav1:
    if st.button("← 메인으로", use_container_width=True):
        # 메인 페이지로 돌아가는 로직 (실제로는 페이지 라우팅 필요)
        st.info("메인 페이지로 돌아갑니다")

with col_nav3:
    if st.button("🔄 퀴즈 다시하기", use_container_width=True):
        reset_quiz()
        st.rerun()

# 현재 문제와 점수 표시
if st.session_state.current_question < len(st.session_state.quiz_questions):
    current_q = st.session_state.quiz_questions[st.session_state.current_question]
    
    # 점수 표시
    progress_col1, progress_col2 = st.columns([3, 1])
    with progress_col1:
        progress = (st.session_state.current_question + 1) / len(st.session_state.quiz_questions)
        st.progress(progress)
        st.write(f"문제 {st.session_state.current_question + 1} / {len(st.session_state.quiz_questions)}")
    
    with progress_col2:
        st.markdown(f"""
        <div class="score-display">
            점수: {st.session_state.score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 3면도 표시
    st.markdown("### 📋 주어진 도면")
    
    drawing_col1, drawing_col2, drawing_col3 = st.columns(3)
    
    with drawing_col1:
        st.markdown(f"""
        <div class="drawing-card">
            <div class="drawing-title">정면도</div>
            <div style="font-family: monospace; font-size: 1.5rem; line-height: 1.2;">
                {current_q['front_view'].replace(chr(10), '<br>')}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with drawing_col2:
        st.markdown(f"""
        <div class="drawing-card">
            <div class="drawing-title">평면도</div>
            <div style="font-family: monospace; font-size: 1.5rem; line-height: 1.2;">
                {current_q['top_view'].replace(chr(10), '<br>')}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with drawing_col3:
        st.markdown(f"""
        <div class="drawing-card">
            <div class="drawing-title">우측면도</div>
            <div style="font-family: monospace; font-size: 1.5rem; line-height: 1.2;">
                {current_q['right_view'].replace(chr(10), '<br>')}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 다음 중 올바른 입체도형을 선택하세요")
    
    # 답안 선택지
    option_cols = st.columns(4)
    
    for i, option in enumerate(current_q['options']):
        with option_cols[i]:
            # 답안 상태에 따른 스타일 클래스 결정
            card_class = "answer-card"
            if st.session_state.answered:
                if option == current_q['correct_answer']:
                    card_class += " answer-correct"
                elif option == st.session_state.selected_answer and option != current_q['correct_answer']:
                    card_class += " answer-wrong"
            elif st.session_state.selected_answer == option:
                card_class += " answer-selected"
            
            st.markdown(f"""
            <div class="{card_class}">
                <div class="shape-display">{option}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # 답안 선택 버튼
            if not st.session_state.answered:
                if st.button(f"선택", key=f"option_{i}", use_container_width=True):
                    st.session_state.selected_answer = option
                    st.rerun()
    
    # 답안 확인 버튼
    if st.session_state.selected_answer and not st.session_state.answered:
        st.markdown("---")
        col_confirm1, col_confirm2, col_confirm3 = st.columns([1, 1, 1])
        with col_confirm2:
            if st.button("✅ 답안 확인", use_container_width=True, type="primary"):
                st.session_state.answered = True
                if st.session_state.selected_answer == current_q['correct_answer']:
                    st.session_state.score += 1
                st.rerun()
    
    # 결과 표시 및 다음 문제 버튼
    if st.session_state.answered:
        st.markdown("---")
        if st.session_state.selected_answer == current_q['correct_answer']:
            st.success(f"🎉 정답입니다! 올바른 답: {current_q['description']}")
        else:
            st.error(f"😅 틀렸습니다. 정답: {current_q['correct_answer']} ({current_q['description']})")
        
        # 해설 추가
        with st.expander("💡 해설 보기"):
            st.write(f"""
            **정답**: {current_q['correct_answer']} ({current_q['description']})
            
            **해설**: 
            - 정면도: 앞에서 본 모양
            - 평면도: 위에서 본 모양  
            - 우측면도: 오른쪽에서 본 모양
            
            이 세 개의 도면을 종합하여 입체도형의 모양을 상상해보세요!
            """)
        
        # 다음 문제 버튼
        col_next1, col_next2, col_next3 = st.columns([1, 1, 1])
        with col_next2:
            if st.session_state.current_question < len(st.session_state.quiz_questions) - 1:
                if st.button("➡️ 다음 문제", use_container_width=True, type="primary"):
                    next_question()
                    st.rerun()
            else:
                if st.button("🏁 결과 보기", use_container_width=True, type="primary"):
                    st.session_state.quiz_completed = True
                    st.rerun()

# 퀴즈 완료 화면
else:
    if 'quiz_completed' in st.session_state and st.session_state.quiz_completed:
        st.balloons()
        
        # 최종 결과
        total_questions = len(st.session_state.quiz_questions)
        score_percentage = (st.session_state.score / total_questions) * 100
        
        st.markdown(f"""
        <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #fbbf24, #f59e0b); border-radius: 20px; color: white;">
            <h1>🎊 퀴즈 완료!</h1>
            <h2>최종 점수: {st.session_state.score} / {total_questions}</h2>
            <h3>정답률: {score_percentage:.1f}%</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 성과 평가
        if score_percentage >= 80:
            st.success("🌟 훌륭합니다! 정투상법을 매우 잘 이해하고 있네요!")
        elif score_percentage >= 60:
            st.info("👍 좋습니다! 조금 더 연습하면 완벽해질 거예요!")
        else:
            st.warning("💪 연습이 더 필요해요! 다시 도전해보세요!")
        
        # 다시하기 버튼
        col_final1, col_final2, col_final3 = st.columns([1, 1, 1])
        with col_final2:
            if st.button("🔄 다시 도전하기", use_container_width=True, type="primary"):
                st.session_state.quiz_completed = False
                reset_quiz()
                st.rerun()

# 사이드바 - 학습 팁
with st.sidebar:
    st.markdown("### 📚 정투상법 학습 팁")
    st.info("""
    **정투상법이란?**
    - 입체도형을 평면에 나타내는 방법
    - 정면도, 평면도, 우측면도 세 가지 시점으로 표현
    
    **문제 풀이 팁:**
    1. 각 면도를 차례대로 분석
    2. 공통 부분을 찾아보기
    3. 머릿속으로 3D 형태 상상하기
    4. 각 선택지와 비교해보기
    """)
    
    if st.session_state.current_question < len(st.session_state.quiz_questions):
        st.markdown("### 📊 현재 진행상황")
        st.write(f"문제: {st.session_state.current_question + 1}/{len(st.session_state.quiz_questions)}")
        st.write(f"점수: {st.session_state.score}")
        
        if st.session_state.selected_answer:
            st.write(f"선택한 답: {st.session_state.selected_answer}")