import streamlit as st
import pandas as pd
import os

CSV_FILE = "data.csv"

# CSVファイルの読み込み（なければ空のDataFrame）
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["名前", "年齢"])

st.title("CSVデータの表示")
st.dataframe(df)