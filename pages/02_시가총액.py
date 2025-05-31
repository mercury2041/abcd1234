import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import datetime
import pandas as pd

st.set_page_config(page_title="실시간 시가총액 분석", layout="wide")
st.title("📈 전 세계 시가총액 TOP 10 기업 - 최근 3년간 추이")

# 기업 티커 및 발행 주식 수 (단위: 주)
companies = {
    "AAPL": {"name": "Apple", "shares_outstanding": 15.8e9},
    "MSFT": {"name": "Microsoft", "shares_outstanding": 7.5e9},
    "2222.SR": {"name": "Saudi Aramco", "shares_outstanding": 219e9},
    "GOOGL": {"name": "Alphabet", "shares_outstanding": 13.1e9},
    "AMZN": {"name": "Amazon", "shares_outstanding": 10.3e9},
    "NVDA": {"name": "NVIDIA", "shares_outstanding": 2.47e9},
    "BRK-B": {"name": "Berkshire Hathaway", "shares_outstanding": 2.21e9},
    "META": {"name": "Meta", "shares_outstanding": 2.56e9},
    "TSM": {"name": "TSMC", "shares_outstanding": 25.9e9},
    "TSLA": {"name": "Tesla", "shares_outstanding": 3.18e9},
}

# 날짜 설정 (3년 전 ~ 오늘)
end = datetime.date.today()
start = end - datetime.timedelta(days=3*365)

# 시가총액 데이터 저장
market_caps = {}

with st.spinner("데이터 불러오는 중..."):
    for ticker, info in companies.items():
        data = yf.download(ticker, start=start, end=end)
        if not data.empty:
            data["MarketCap"] = data["Close"] * info["shares_outstanding"] / 1e12  # 단위: 조 달러
            market_caps[info["name"]] = data["MarketCap"]

# 병합
df = pd.DataFrame(market_caps)
df = df.dropna(how="all")

# Plotly 시각화
fig = go.Figure()
for company in df.columns:
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df[company],
        mode="lines",
        name=company
    ))

fig.update_layout(
    title="전 세계 시가총액 TOP 10 기업의 실시간 변화 (단위: 조 달러)",
    xaxis_title="날짜",
    yaxis_title="시가총액",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
