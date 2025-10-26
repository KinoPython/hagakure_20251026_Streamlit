import streamlit as st

st.title("クエリパラメータの例")

# 単独パラメータ: ?name=太郎
name = st.query_params.get("name", "")
st.write(f"私の名前は{name}です。")

# 複数パラメータ: ?city=Tokyo&tag=sushi
city = st.query_params.get("city", "")
tag = st.query_params.get("tag", "")
st.write(f"出身は{city}、好きなものは{tag}です。")