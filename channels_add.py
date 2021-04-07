import pandas
import json
import os


yt_key = os.environ["YT_KEY"]

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
#append row to the dataframe
df = pd.read_csv("channels.csv")
df = df.append(new_row, ignore_index=True)
df.to_csv("channels.csv",index=False)
