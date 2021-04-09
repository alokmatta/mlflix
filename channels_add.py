import pandas as pd
import json
import os
from urllib.request import urlopen
import re
import sys

yt_key = os.environ["YT_KEY"]


def url_extract(text):

    return(re.search("(?P<url>https?://[^\s]+)", text).group("url"))


def url_type(url):
    type = "channel"
    if url.find("/user/") != -1:
        type = "user"
    if url.find("/c/") != -1:
        type = "custom"

    return type


df = pd.read_csv("links.txt", header=None, names=["text"])
df_channels = pd.read_csv("channels.csv")
df["url"] = df.text.apply(url_extract)
df["type"] = df.url.apply(url_type)


df = df[df["url"].str.contains("youtube.com")]
df = df[~df["url"].str.contains("playlist")]
df = df[~df["url"].str.contains("watch")]
df.reset_index(inplace=True)

df.to_csv("links.csv", index=False)

for i in range(40, 50):
    print(df.url[i])
    url_list = df.url[i].split("/")
    print(url_list)
    if df.type[i] == "user":
        name = url_list[url_list.index("user")+1]
        url = "https://www.googleapis.com/youtube/v3/channels?forUsername="+name+"&key="+yt_key
        # print(url)
        json_str = urlopen(url).read()
        channel_id = json.loads(json_str)["items"][0]["id"]

    elif df.type[i] == "custom":
        name = url_list[url_list.index("c")+1]
        url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key + \
              "&q="+name+"&part=snippet,id&order=date&maxResults=5&type=channel"
        # print(url)
        json_str = urlopen(url).read()
        if(json.loads(json_str)["items"]):
            channel_id = json.loads(json_str)["items"][0]["id"]["channelId"]
            name = json.loads(json_str)["items"][0]["snippet"]["channelTitle"]
        else:
            print(f"custom user {name} has no channels")
    elif df.type[i] == "channel":
        channel_id = url_list[url_list.index("channel")+1]
        text_list = df.text[i].split("-")
        name = text_list[0]

    if(channel_id):
        if channel_id not in df_channels.channel_id.values:
            new_row = {'name': name, 'channel_id': channel_id}
            print("adding new row", new_row)
            # #append row to the dataframe
            df_channels = df_channels.append(new_row, ignore_index=True)
        else:
            print(f"channel {name} already exists")
    print("")
    print("")
df_channels.to_csv("channels.csv", index=False)