import warnings
import numpy as np

# numpy の互換性警告を抑制
warnings.filterwarnings('ignore', category=FutureWarning)

# numpy.bool の問題を回避
if not hasattr(np, 'bool'):
    np.bool = bool
if not hasattr(np, 'int'):
    np.int = int
if not hasattr(np, 'float'):
    np.float = float
if not hasattr(np, 'complex'):
    np.complex = complex
if not hasattr(np, 'object'):
    np.object = object
if not hasattr(np, 'unicode'):
    np.unicode = str
if not hasattr(np, 'str'):
    np.str = str

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