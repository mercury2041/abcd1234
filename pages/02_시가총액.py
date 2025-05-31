import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="전 세계 시가총액 TOP 10 (3년 변화)", layout="wide")

st.title("📈 전 세계 시가총액 TOP 10 기업의 3년간 변화")
st.write("아래 그래프는 상위 10개 기업의 시가총액 추이를 보여줍니다. (데이터는 예시입니다)")

# 가상의 연도별 시가총액 데이터 (단위: 조 달러)
companies = ["Apple", "Microsoft", "Saudi Aramco", "Alphabet", "Amazon", "NVIDIA", "Berkshire Hathaway", "Meta", "TSMC", "Tesla"]
years = ["2022", "2023", "2024"]

# 예시 데이터 (실제 데이터 아님)
market_cap = {
    "Apple": [2.8, 2.9, 3.0],
    "Microsoft": [2.3, 2.5, 2.8],
    "Saudi Aramco": [2.0, 2.1, 2.2],
    "Alphabet": [1.6, 1.7, 1.9],
    "Amazon": [1.5, 1.4, 1.6],
    "NVIDIA": [0.8, 1.2, 2.2],
    "Berkshire Hathaway": [0.7, 0.8, 0.9],
    "Meta": [0.9, 0.6, 1.2],
    "TSMC": [0.6, 0.5, 0.6],
    "Tesla": [0.8, 0.6, 0.7]
}

# Plotly 그래프 생성
fig = go.Figure()

for company in companies:
    fig.add_trace(go.Scatter(
        x=years,
        y=market_cap[company],
        mode='lines+markers',
        name=company
    ))

fig.update_layout(
    title="전 세계 시가총액 TOP 10 기업의 시가총액 추이 (2022~2024)",
    xaxis_title="연도",
    yaxis_title="시가총액 (조 달러)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
