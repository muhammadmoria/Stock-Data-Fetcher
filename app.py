import streamlit as st
import yfinance as yf
from datetime import date

# --- App Configuration ---
st.set_page_config(
    page_title="StockFlow",  # Updated name here
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom Styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #ecf0f1;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        font-size: 40px;
        text-align: center;
        color: #2C3E50;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .big-font {
        font-size: 24px;
        text-align: center;
        color: #34495E;
        margin-bottom: 40px;
    }
    .metric-box {
        background: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 20px;
    }
    .sidebar .sidebar-content {
        padding-top: 50px;
    }
    .stButton button {
        background-color: #3498DB;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    footer {visibility: hidden;}
    .about-me-box {
        background: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-size: 20px;
        margin-bottom: 30px;
    }
    .about-me-title {
        text-align: center;
        font-size: 30px;
        color: #2C3E50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .about-me-description {
        color: #7F8C8D;
        text-align: justify;
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar Branding ---
with st.sidebar:
    st.markdown(
        "<h1 style='color: #3498DB; text-align: center;'> StockFlow 💹</h1>",
        unsafe_allow_html=True,
    )
    st.info(
        "Welcome to **StockFlow**, a professional platform for fetching and downloading stock market data easily. Start exploring the market now!"
    )
    st.markdown("---")
    # Add an About Me tab in sidebar
    about_me = st.selectbox("Select a Section", ["Fetch Stock Data", "About Me"])

# --- App Header ---
st.markdown("<h1>Welcome to StockFlow 💰</h1>", unsafe_allow_html=True)
st.markdown("<p class='big-font'>Fetch and Download Stock Data Effortlessly</p>", unsafe_allow_html=True)

# --- Data Fetcher Section ---
if about_me == "Fetch Stock Data":
    st.markdown("## 🔍 Fetch Historical Stock Data")

    # --- Stock Ticker Input ---
    stock_list = [
        "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "BRK-B", "NVDA", "JPM", "V",
        "UNH", "XOM", "MA", "HD", "PG", "NFLX", "LLY", "WMT", "TSM", "DIS"
    ]
    selected_ticker = st.selectbox("Select a Stock Ticker", stock_list)

    # --- Date Range Input ---
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date:", value=date(2015, 1, 1))
    with col2:
        end_date = st.date_input("End Date:", value=date.today())

    # --- Fetch Data Button ---
    if st.button("Fetch Stock Data"):
        with st.spinner("Fetching data... please wait."):
            data = yf.download(selected_ticker, start=start_date, end=end_date)

        if not data.empty:
            st.success("🎉 Data fetched successfully!")
            st.dataframe(data.reset_index(), use_container_width=True)

            # --- Download CSV Button ---
            csv_data = data.to_csv(index=True)
            st.download_button(
                label="💾 Download Data as CSV",
                data=csv_data,
                file_name=f"{selected_ticker}_data.csv",
                mime="text/csv",
            )
        else:
            st.warning("⚠ No data available for the selected date range!")

elif about_me == "About Me":
    # --- About Me Section ---
    st.markdown("<h1 class='about-me-title'>About Me</h1>", unsafe_allow_html=True)

    st.markdown(
        "<div class='about-me-box'>"
        "<p class='about-me-description'>"
        "Hi, I'm <strong> Muhammad Dawood</strong>, a Data Scientist, Machine Learning Engineer. "
        "I specialize in building advanced AI, Data Science, and ML applications that create real value for businesses. "
        "I have a strong passion for data analytics and AI-driven decision making, helping businesses leverage data insights for growth. "
        "I believe in empowering organizations by transforming data into actionable strategies. "
        "Currently, I'm focused on bringing innovative solutions in the fields of machine learning, NLP, and web development. "
        "Feel free to connect with me on <a href='https://www.linkedin.com/in/muhammadmoria/' target='_blank'>LinkedIn</a> for collaborations or projects!"
        "<a href='https://www.github.com/muhammadmoria' target='_blank'>Github</a>"
        "</p>"
        "</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <hr>
    <p style="text-align: center; color: #95A5A6;">
    Built with ❤️ by <a href="https://www.linkedin.pk/muhammadmoria" target="_blank">Muhammad Dawood</a>
    </p>
    """,
    unsafe_allow_html=True,
)
