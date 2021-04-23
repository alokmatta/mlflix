import pandas as pd
import json
import os


yt_key = os.environ["YT_KEY"]

yt_key2 = os.environ["YT_KEY2"]

df_channels = pd.read_csv("channels.csv")

df_list = []

#for i in range(0,len(df_channels)):
for i in range(0,100):

    if i%2:
        yt_key = yt_key2
        key_str = "Key2"
    else:
        key_str = "Key1"

    url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key + \
        "&channelId="+df_channels.channel_id[i]+"&part=snippet,id&order=date&maxResults=5&type=video"
    # print(url)
    print("fetching channel", df_channels.name[i], "using", key_str)
    from urllib.request import urlopen
    json_str = urlopen(url).read()
    df_list.append(pd.json_normalize(json.loads(json_str)["items"]))

df = pd.concat(df_list)
df.to_csv("videos.csv")
