from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import base64

st.set_page_config(
    layout="wide", page_title="MLFix & Chill!", initial_sidebar_state="expanded"
)

"""
# MLFlix & Chill!

"""


yt_key="AIzaSyDtdRxtBGzTg1muYuyafE8jVe3GJdDOllk"

#url = "https://www.googleapis.com/youtube/v3/channels?forUsername="+forUsername+"&key="+yt_key
#forUsername = "PyDataTV"
#from urllib.request import urlopen
#json_str = urlopen(url).read()
#channel_id=json.loads(json_str)["items"][0]["id"]

channelDict = {}
channelDict["PyData"] = "UCOjD18EJYcsBog4IozkF_7w"
channelDict["PyCascades"] = "UCtWI06j1EADmEOGj2iJhSyA"
channelDict["PyDataPune"] = "UCEnagt088yX-ruTalg-GJeQ"
channelDict["PyData MCR"] = "UCTCV2vonJgaQVb8AdMgdvCA"
channelDict["PyLondinium"] = "UCTCV2vonJgaQVb8AdMgdvCA"
channelDict["PyData Montreal"] = "UC2d_azMgPLw_8JzgbpNb2oQ"
channelDict["Deepmind"] = "UCP7jMXSY2xbc3KCAE0MHQ-A"
channelDict["AICamp"] = "UCj09XsAWj-RF9kY4UvBJh_A"
channelDict["NLPXing"] = "UCuGC1JusVvbOGa__qMtH3QA"
channelDict["W&B"] = "UCBp3w4DCEC64FZr4k9ROxig"
channelDict["London ML"] = "UCpwC9QC0lWaEJ85MoMRFvrA"
channelDict["Yannic Kilcher"] = "UCZHmQk67mSJgfCCTn7xBfew"





st.beta_container()

col1, col2 = st.beta_columns(2)
#col1.subheader('Col1')
#col1.subheader('Col2')

for name, channel_id in channelDict.items():    
    with st.beta_expander(name):
        url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key+"&channelId="+channel_id+"&part=snippet,id&order=date&maxResults=5&type=video"
        #print(url)
        from urllib.request import urlopen
        json_str = urlopen(url).read()


        df = pd.json_normalize(json.loads(json_str)["items"])

        for i in range(0,len(df)):
            url = df["snippet.thumbnails.medium.url"][i]
            image_base64 = base64.b64encode(urlopen(url).read()).decode('utf-8')

            from urllib.request import urlopen
            from PIL import Image

            #img = Image.open(urlopen(url))
            #st.text(df["snippet.channelTitle"][i])
            st.text(df["snippet.description"][i])
            link = url = "http://www.youtube.com/watch?v="+df["id.videoId"][i]
            html = f"<a href='{link}'><img src='data:image/png;base64,{image_base64}'></a>"
            st.markdown(html, unsafe_allow_html=True)
