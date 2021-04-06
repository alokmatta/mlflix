from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import base64

"""
# MLFix & Chill!

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

for channel_id in channelDict.values():
    url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key+"&channelId="+channel_id+"&part=snippet,id&order=date&maxResults=5&type=video"
    print(url)
    from urllib.request import urlopen
    json_str = urlopen(url).read()


    df = pd.json_normalize(json.loads(json_str)["items"])

    for i in range(0,len(df)):
        url = df["snippet.thumbnails.medium.url"][i]
        image_base64 = base64.b64encode(urlopen(url).read()).decode('utf-8')

        from urllib.request import urlopen
        from PIL import Image

        #img = Image.open(urlopen(url))
        st.text(df["snippet.channelTitle"][i])
        st.text(df["snippet.description"][i])
        link = url = "http://www.youtube.com/watch?v="+df["id.videoId"][i]
        html = f"<a href='{link}'><img src='data:image/png;base64,{image_base64}'></a>"
        st.markdown(html, unsafe_allow_html=True)
