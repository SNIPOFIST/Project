# the streamlit is imported and set an alias st
# the yfinance is imported and set an alias yf
# click on "Deploy this app "
# click a github repo 


import datetime
from datetime import timedelta
import time 
import streamlit as st
import yfinance as yf


description_txt = """This Dashboard is an experimental visualisation dashboard for viewing 
the Open, High, Low, Close, Volume and other such data of a selected stock symbol.\n 
This Data represented below was imported using the 'yfinance' Python Library.\n
Tool used\n
\tStreamlit : Web interface 
\tYahoo finance python library (yfinance) : Realtime stock market data source
"""

st.set_page_config(
    layout = "wide",
    menu_items = {
        'About' : description_txt}
)

st.title(""" 
            Stock Price Analysis :bar_chart:""")


today_yyy_mm_d = datetime.date.today()
today_year = today_yyy_mm_d.strftime("%Y")
today_month = today_yyy_mm_d.strftime("%m")
today_date = today_yyy_mm_d.strftime("%d")
yesterday = today_yyy_mm_d - timedelta(days=1)



symbol = st.selectbox(
    'Which Stock Symbol would you want to analyse?',
    ('AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META', 'TSLA', 'GOOG', 'FB', 'JPM', 'BABA',
'PG', 'NVDA', 'UNH', 'HD', 'WMT', 'DIS', 'MA', 'V', 'TSM', 'INTC', 'BA',
'CSCO', 'JNJ', 'MRK', 'WBA', 'KO', 'PEP', 'XOM', 'CMCSA', 'DISN', 'T',
'UPS', 'CAT', 'PGN', 'UNH', 'VZ', 'MSFT', 'ABT', 'KO', 'WMT', 'TGT',
'COST', 'HD', 'LOW', 'CVS', 'WMT', 'BRK.A', 'BRK.B', 'TRV', 'UNH', 'PM',
'VZ', 'JNJ', 'EMR', 'MMM', 'CAT', 'AAPL', 'UNH', 'PG', 'MRK', 'CVX',
'JPM', 'WBA', 'PFE', 'ABT', 'LLY', 'COST', 'WMT'))


ticker_data = yf.Ticker(symbol)



current_price ="{} {}".format(ticker_data.info['currentPrice'],ticker_data.info['financialCurrency'])
st.header("Stock current value : {}".format(current_price))

business_story = ticker_data.info['longBusinessSummary']

if st.button('About {} 🔎'.format(symbol)):
    st.caption(business_story)


col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start date", datetime.date(2023, 1, 1))

with col2:
    end_date = st.date_input("End date", datetime.date(int(today_year), int(today_month), int(today_date)))


ticker_df = ticker_data.history(period="1d", start= start_date, end=end_date)
st.dataframe(ticker_df)

st.write(f"""
    ### {symbol}'s Closing Price Chart""")

st.line_chart(ticker_df["Close"])

st.write(f"""
    ### {symbol}'s Volume Chart""")

st.line_chart(ticker_df["Volume"])
