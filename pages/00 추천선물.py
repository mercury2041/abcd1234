import streamlit as st

# MBTI별 선물 추천
mbti_gifts = {
    "INTJ": "📓 고급 노트 + 만년필 세트",
    "INTP": "🧩 창의력 자극 퍼즐 + 독특한 책",
    "ENTJ": "⌚ 세련된 시계 + 스마트 오거나이저",
    "ENTP": "🎲 보드게임 + 이색 체험권",

    "INFJ": "🕯️ 향초 + 힐링 에세이",
    "INFP": "📖 감성 시집 + 감성 머그컵",
    "ENFJ": "🎁 맞춤형 플래너 + 따뜻한 담요",
    "ENFP": "🎨 컬러링북 + 아트 키트",

    "ISTJ": "📦 실용적인 멀티툴 + 클래식 지갑",
    "ISFJ": "🍪 홈메이드 베이킹 키트 + 손편지",
    "ESTJ": "🗂️ 데스크 정리 세트 + 커피 구독권",
    "ESFJ": "🌷 꽃다발 + 사진 앨범",

    "ISTP": "🛠️ 미니 공구세트 + DIY 키트",
    "ISFP": "🖼️ 감성 인테리어 소품 + 음악 앨범",
    "ESTP": "🎧 블루투스 이어폰 + 익스트림 체험권",
    "ESFP": "💄 뷰티 키트 + 스타일리시 액세서리"
}

# Streamlit 앱 시작
st.title("🎁 MBTI 선물 추천기")

st.write("당신의 MBTI에 딱 맞는 선물을 추천해드릴게요!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_gifts.keys()))

# 추천 출력
if mbti:
    st.subheader("🎉 추천 선물:")
    st.success(mbti_gifts[mbti])
