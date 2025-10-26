import streamlit as st

# 必ず最初の行で呼び出す（他のst.〇〇より前）
st.set_page_config(
    page_title="私のアプリ",
    page_icon="📝",
    layout="wide"  # 画面幅いっぱい（デフォルトは"centered"）
)

# ここから通常のコード
# .streamlit/config.toml の配色が自動で反映される
st.title("📝 私のアプリ")
st.write("ブラウザタブのタイトルとアイコンが設定されています")
st.button("ボタンの色は config.toml の primaryColor")