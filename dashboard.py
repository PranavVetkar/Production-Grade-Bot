import streamlit as st
import pandas as pd
import sqlite3

st.title("🛡️ Production Bot Dashboard")

def load_data():
    conn = sqlite3.connect("crypto_trading.db")
    df = pd.read_sql_query("SELECT * FROM trade_log ORDER BY id DESC", conn)
    conn.close()
    return df

if st.button('Refresh Data'):
    data = load_data()
    st.write("### Trade History")
    st.dataframe(data)
    st.write("### Balance Over Time")
    st.line_chart(data.set_index('timestamp')['balance'])