from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import base64
from urllib.request import urlopen
from PIL import Image
import random
import numpy as np

st.set_page_config(
    layout="wide", page_title="MLFix & Chill!"
)

"""
# MLFlix & Chill!
"""


df_all = pd.read_csv("videos.csv")

st.container()

col1, col2 = st.beta_columns(2)
#col1.subheader('Col1')
#col1.subheader('Col2')

                
names = df_all["snippet.channelTitle"].unique()

for name in random.sample(list(names), 5):
    with st.beta_expander(name):
        df = df_all[df_all["snippet.channelTitle"]==name]
        df.reset_index(inplace=True)
        header =    """
                    |   Image        | Description |
                    | --------- | ----------- |
                    """

        rows = ""
        for i in range(0,len(df)):
  
            url = df["snippet.thumbnails.medium.url"][i]
            image_base64 = base64.b64encode(urlopen(url).read()).decode('utf-8')

            #img = Image.open(urlopen(url))
            #name =st.text(df["snippet.channelTitle"][i])
            #st.text(df["snippet.description"][i])
            description = df["snippet.description"][i]
        
            if(len(str(description))>3):
                #print(len(str(description)))
                split = " "
                des_list= description.split(split)
                if(len(des_list)>200):
                  description= split.join(des_list[0:200])
            elif(np.isnan(float(description))):
                description = ""
            
            link = url = "http://www.youtube.com/watch?v="+df["id.videoId"][i]
            image = f"<a href='{link}' target=”_blank”><img src='data:image/png;base64,{image_base64}'></a>"
            description = f"<a href='{link}' target=”_blank”>{description}</a>"
            rows += f"| {image}      |    {description}   |\n"
        html = header + rows
        st.markdown(html, unsafe_allow_html=True)
