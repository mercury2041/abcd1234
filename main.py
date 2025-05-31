import streamlit as st

# MBTI별 추천 여행 코스
mbti_travel = {
    "INTJ": "📚 조용한 서점 투어 + 미술관 관람",
    "INTP": "🧠 과학 박물관 + 철학 산책 코스",
    "ENTJ": "🏙️ 도시 비즈니스 투어 + 고급 레스토랑",
    "ENTP": "🎭 이색 전시회 + 즉흥 거리 공연 감상",

    "INFJ": "🌲 숲속 힐링 여행 + 조용한 카페 탐방",
    "INFP": "📖 감성 골목 산책 + 독립 서점 탐방",
    "ENFJ": "🎤 문화 체험 프로그램 + 지역 봉사 활동",
    "ENFP": "🎨 예술 벽화 거리 + 야시장 투어",

    "ISTJ": "🏛️ 역사 유적지 탐방 + 전통 음식 체험",
    "ISFJ": "🪴 식물원 + 소도시 정원 여행",
    "ESTJ": "🚆 계획된 당일치기 투어 + 지역 특산품 시장",
    "ESFJ": "🎡 테마파크 + 지역 유명 맛집 투어",

    "ISTP": "🧗 액티비티 체험 + 드라이브 코스",
    "ISFP": "🌅 감성 바닷가 산책 + 노을 명소",
    "ESTP": "🏄 익스트림 스포츠 + 핫플레이스 방문",
    "ESFP": "🎉 축제 참여 + 트렌디 카페 투어"
}

# Streamlit 앱
st.title("✈️ MBTI 여행 추천기")

st.write("당신의 MBTI를 선택하면, 어울리는 여행 코스를 추천해드릴게요!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_travel.keys()))

# 추천 결과 출력
if mbti:
    st.subheader("📍 추천 여행 코스:")
    st.success(mbti_travel[mbti])

