from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import base64
from urllib.request import urlopen
from PIL import Image

st.set_page_config(
    layout="wide", page_title="MLFix & Chill!", initial_sidebar_state="expanded"
)

"""
# MLFlix & Chill!

"""


df_all = pd.read_csv("videos.csv")

st.beta_container()

col1, col2 = st.beta_columns(2)
#col1.subheader('Col1')
#col1.subheader('Col2')

for name in df_all["snippet.channelTitle"].unique():
    with st.beta_expander(name):
        df = df_all[df_all["snippet.channelTitle"]==name]
        df.reset_index(inplace=True)
        for i in range(0,len(df)):
            url = df["snippet.thumbnails.medium.url"][i]
            image_base64 = base64.b64encode(urlopen(url).read()).decode('utf-8')

            #img = Image.open(urlopen(url))
            #name =st.text(df["snippet.channelTitle"][i])
            st.text(df["snippet.description"][i])
            link = url = "http://www.youtube.com/watch?v="+df["id.videoId"][i]
            html = f"<a href='{link}'><img src='data:image/png;base64,{image_base64}'></a>"
            st.markdown(html, unsafe_allow_html=True)
