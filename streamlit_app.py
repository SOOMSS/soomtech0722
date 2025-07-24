import streamlit as st

st.set_page_config(page_title="📘 마인크래프트 블록쌓기 가이드", layout="centered")
st.title("📘 마인크래프트 블록쌓기 기초 가이드")

st.markdown("""
## 🧱 마인크래프트란?

**마인크래프트(Minecraft)**는 Mojang Studios에서 개발한 샌드박스 형식의 게임으로, 블록을 쌓아 나만의 세계를 만들 수 있는 게임입니다. 건축, 탐험, 생존, 창의적인 표현 등 다양한 활동이 가능하며, 교육적으로도 코딩, 설계, 문제해결력 향상에 많이 활용됩니다.

![Minecraft Screenshot 1](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150201_96%2Fchlrbgus33_1422780473330VLBMV_PNG%2F20150201_172757.png&type=sc960_832)

---

## 🔧 기본 조작 방법

- **이동**: W, A, S, D 키로 앞뒤좌우 이동
- **점프**: 스페이스바
- **블록 부수기**: 마우스 왼쪽 클릭
- **블록 놓기**: 마우스 오른쪽 클릭
- **블록 선택**: 1~9 숫자 키 또는 마우스 휠
![Minecraft Screenshot 1](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTAyMjhfMTIy%2FMDAxNzQwNzIwMTcwNTU1.FsMFST_REWr8Ju1LCY3KeLuXZKZ5UuSol-lOBrJ6G08g.d1uCTOZLC13kIdBMxLJkgJ4v5WOvi3y3yMm0s-aCS40g.PNG%2F%25B8%25B6%25C0%25CE%25C5%25A9%25B7%25A1%25C7%25C1%25C6%25AE_%25C3%25CA%25BA%25B8%25C0%25DA_%25C8%25B0%25BF%25EB%25B9%25FD_%25C4%25C4%25C7%25BB%25C5%25CD_%25BB%25E7%25BF%25EB%25BD%25C3_%25C1%25B6%25C0%25DB%25B9%25FD.png&type=sc960_832)
---

## 🧱 기본 블록쌓기 예제

아래는 마인크래프트 내에서 코딩으로 간단한 벽을 만드는 Python 예시입니다 (Minecraft Education Edition + Code Builder 기반):

```python
from minecraftstuff import MinecraftShape
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

# 가로 5칸, 높이 3칸의 벽 만들기
for i in range(5):
    for j in range(3):
        mc.setBlock(x + i, y + j, z, block.STONE)
```

---

## 🪵 추천 건축 블록

| 블록 이름 | 설명 |
|-----------|------|
| Oak Planks | 나무 재질, 초보자용 기본 블록 |
| Stone Bricks | 내구도 강하고 깔끔한 벽체에 적합 |
| Glass | 창문 및 투명 장식에 적합 |
| Concrete | 다양한 색상으로 외관 꾸미기에 유용 |
| Glowstone | 조명 역할, 밤에 빛나는 블록 |

![Minecraft Screenshot 1](https://postfiles.pstatic.net/20150218_141/ljaewoo04_1424255310398OVJnF_PNG/2015-02-18_03.03.13.png?type=w1)
---

## 🏗️ 건축 팁

- 기본 단위는 1블록 (1m³)
- 문은 세로로 2블록 크기
- 캐릭터 키는 약 1.8블록
- 지붕은 사다리꼴 형태 또는 계단 블록 활용
- 창문은 투명 블록으로 표현 가능
- 레드스톤으로 자동문, 불빛 장치 등 구현 가능

---

## 🖼️ 예시 건축 이미지

![Minecraft House](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAyMDhfMjE1%2FMDAxNjc1ODQwNDI5ODc4.BeLR3se5L8qwKmrlwaGWxF_gflz4i4Wbmm0Xh5NH7c4g.e3V6tPcTvddcleOPH3ncQPGgoUd3oTJAFkIOKJ7KK-Qg.JPEG.mswjtg75%2F%25C0%25CC%25C5%25C2%25C0%25B1_%25282%2529.jpg&type=a340)

![Minecraft Interior](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20141113_21%2Fgodgo664_1415866391717BLnM3_PNG%2F2014-11-03_06.55.24.png&type=l340_165)

---

## 📌 요약

- 마인크래프트는 창의력 중심의 설계 교육에 유용
- 기본 조작 및 블록 종류 이해가 핵심
- Python 등 코딩 연계도 가능하며 교육용 활용도 높음

👉 다음 단계: 🏠 design 페이지로 이동해서 건축설계를 시작하세요. 
""")
