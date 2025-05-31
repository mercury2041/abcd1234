import streamlit as st

st.set_page_config(page_title="한국인이 사랑하는 여행지 TOP 10", layout="wide")

st.title("🇰🇷 한국인이 사랑하는 여행지 TOP 10")

st.write("한국에서 가장 인기 있는 여행지들을 소개합니다! 도시별 대표 명소와 특징들을 함께 확인해보세요.")

# 여행지 정보 리스트
travel_spots = [
    {"city": "서울", "emoji": "🏙️", "desc": "대한민국의 수도, 전통과 현대가 공존하는 도시. 경복궁, 남산타워, 홍대 등이 인기."},
    {"city": "부산", "emoji": "🌊", "desc": "해운대와 광안리 해변으로 유명한 해양 도시. 감천문화마을도 인기 명소 중 하나."},
    {"city": "제주도", "emoji": "🌴", "desc": "아름다운 자연과 오름, 한라산이 있는 섬. 국내 최대 휴양지로 사랑받는 여행지."},
    {"city": "강릉", "emoji": "⛱️", "desc": "경포대, 안목해변, 커피거리로 유명한 동해안 대표 관광 도시."},
    {"city": "경주", "emoji": "🏛️", "desc": "천년의 역사 도시. 불국사, 첨성대, 대릉원 등 유적지가 많음."},
    {"city": "속초", "emoji": "🦞", "desc": "설악산과 속초 해변이 유명한 도시. 대게와 해산물도 인기."},
    {"city": "전주", "emoji": "🏯", "desc": "한옥마을과 전주비빔밥으로 유명한 전통의 도시."},
    {"city": "여수", "emoji": "🚤", "desc": "바다와 야경이 아름다운 항구 도시. 여수밤바다로 유명함."},
    {"city": "인천", "emoji": "🛫", "desc": "국제공항이 위치한 도시. 차이나타운과 송도 신도시 등 관광지가 많음."},
    {"city": "춘천", "emoji": "🚣", "desc": "닭갈비와 남이섬으로 유명한 낭만 도시. 드라마 촬영지로도 인기."},
]

# 2개씩 나눠서 그리드 형태로 보여주기
for i in range(0, len(travel_spots), 2):
    col1, col2 = st.columns(2)
    
    for col, spot in zip([col1, col2], travel_spots[i:i+2]):
        with col:
            st.subheader(f"{spot['emoji']} {spot['city']}")
            st.write(spot["desc"])
            st.markdown("---")
