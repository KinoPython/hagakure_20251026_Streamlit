import streamlit as st

st.title("🧩 タブ切り替えの例")

tab_input, tab_result = st.tabs(["入力", "結果"]) 

with tab_input:
    name = st.text_input("名前")
    if st.button("保存"):
        st.session_state["name"] = name

with tab_result:
    st.write("入力結果")
    st.write(st.session_state.get("name", "まだ入力されていません"))