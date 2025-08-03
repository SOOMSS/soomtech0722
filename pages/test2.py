import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="건축 설계 도구", layout="wide")

st.markdown("## 🏗️ 외부 설계도구 연동")

components.iframe("https://dashing-lokum-753923.netlify.app/", height=1000, width=1200)
