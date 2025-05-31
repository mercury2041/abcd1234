import streamlit as st
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="시가총액 TOP 10", layout="wide")

st.title("📈 전 세계 시가총액 TOP 10 기업 (2022–2024)")
st.write("아래 그래프는 최근 3년간 전 세계 시가총액 상위 10개 기업의 시가총액 변화를 보여줍니다. (단위: 조 달러, 데이터는 예시입니다)")

# 시가총액 데이터 (가상의 예시 데이터, 단위: 조 달러)
years = ["2022", "2023", "2024"]
companies = {
    "Apple": [2.8, 2.9, 3.0],
    "Microsoft": [2.4, 2.6, 2.9],
    "Saudi Aramco": [2.0, 2.1, 2.2],
    "Alphabet": [1.5, 1.7, 1.9],
    "Amazon": [1.3, 1.4, 1.6],
    "NVIDIA": [0.8, 1.3, 2.2],
    "Berkshire Hathaway": [0.7, 0.9, 1.0],
    "Meta": [0.9, 0.8, 1.3],
    "TSMC": [0.6, 0.65, 0.7],
    "Tesla": [0.9, 0.7, 0.8],
}

# Plotly 그래프 생성
fig = go.Figure()

for name, values in companies.items():
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers",
        name=name
    ))

fig.update_layout(
    title="시가총액 상위 10개 기업의 3년간 변화",
    xaxis_title="연도",
    yaxis_title="시가총액 (조 달러)",
    hovermode="x unified",
    template="plotly_white"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
