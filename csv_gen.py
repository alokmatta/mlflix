import pandas as pd
import json
import os

#yt_key="AIzaSyDtdRxtBGzTg1muYuyafE8jVe3GJdDOllk"

#yt_key="AIzaSyArlqkjBGy9KTW2TjT0qsCHzx0-dp1UJnw"

yt_key = os.env["yt_key"]

#url = "https://www.googleapis.com/youtube/v3/channels?forUsername="+forUsername+"&key="+yt_key
#forUsername = "PyDataTV"
#from urllib.request import urlopen
#json_str = urlopen(url).read()
#channel_id=json.loads(json_str)["items"][0]["id"]

channelDict = {}
channelDict["PyData"] = "UCOjD18EJYcsBog4IozkF_7w"
channelDict["PyCascades"] = "UCtWI06j1EADmEOGj2iJhSyA"
# channelDict["PyDataPune"] = "UCEnagt088yX-ruTalg-GJeQ"
# channelDict["PyData MCR"] = "UCTCV2vonJgaQVb8AdMgdvCA"
# channelDict["PyLondinium"] = "UCTCV2vonJgaQVb8AdMgdvCA"
# channelDict["PyData Montreal"] = "UC2d_azMgPLw_8JzgbpNb2oQ"
# channelDict["Deepmind"] = "UCP7jMXSY2xbc3KCAE0MHQ-A"
# channelDict["AICamp"] = "UCj09XsAWj-RF9kY4UvBJh_A"
# channelDict["NLPXing"] = "UCuGC1JusVvbOGa__qMtH3QA"
# channelDict["W&B"] = "UCBp3w4DCEC64FZr4k9ROxig"
# channelDict["London ML"] = "UCpwC9QC0lWaEJ85MoMRFvrA"
# channelDict["Yannic Kilcher"] = "UCZHmQk67mSJgfCCTn7xBfew"


for name, channel_id in channelDict.items():    

        url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key+"&channelId="+channel_id+"&part=snippet,id&order=date&maxResults=5&type=video"
        #print(url)
        from urllib.request import urlopen
        json_str = urlopen(url).read()
        
        if 'df' in locals():
          df.append(pd.json_normalize(json.loads(json_str)["items"]))
        else:
          df = pd.json_normalize(json.loads(json_str)["items"])
        
        df.to_csv("videos.csv")
