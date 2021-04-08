import pandas as pd
import json
import os
from urllib.request import urlopen
import re

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
df["url"] = df.text.apply(url_extract)
df["type"] = df.url.apply(url_type)
df.to_csv("links.csv", index=False)

#forUsername=metrostarsystems
#url = "https://www.googleapis.com/youtube/v3/channels?forUsername="+forUsername+"&key="+yt_key
#forUsername = "PyDataTV"
#from urllib.request import urlopen
#json_str = urlopen(url).read()
#channel_id=json.loads(json_str)["items"][0]["id"]

custom = "PyCon2020"
url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key + \
     "&q="+custom+"&part=snippet,id&order=date&maxResults=5&type=channel"
print(url)
json_str = urlopen(url).read()
channel_id=json.loads(json_str)["items"][0]["id"]["channelId"]
name=json.loads(json_str)["items"][0]["snippet"]["channelTitle"]
new_row = {'name':name, 'channel_id':channel_id}
print("adding new row", new_row)
#append row to the dataframe
df = pd.read_csv("channels.csv")
df = df.append(new_row, ignore_index=True)
df.to_csv("channels.csv",index=False)
