import pandas as pd
import json
import os


yt_key = os.environ["YT_KEY"]

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
channelDict["ML Dojo"] = "UCXvHuBMbgJw67i5vrMBBobA"
channelDict["ML OPS"] = "UCG6qpjVnBTTT8wLGBygANOQ"
channelDict["TinyML"] = "UC9iWqvsWjhowkHWVJquHwkg"
channelDict["Usha"] = "UChr1xW6wSq4sxUgAlgv9PZQ"
channelDict["AIEveryone"] = "UCIpPdErVmb3sfCT6S8U3BwA"
channelDict["Wildlabs"] = "UCrxw8iiyFalKHFNAhZYCAYA"
channelDict["Bhavesh"] = "UC8ofcOdHNINiPrBA9D59Vaw"
channelDict["FSDL"] = "UCVchfoB65aVtQiDITbGq2LQ"
channelDict["Zachary Mueller"] = "UCmKoQOD8uBqsRS8XDdSgrlQ"
channelDict["Deeplearning"] = "UCcIXc5mJsHVYTZR1maL5l9w"
channelDict["ECCV"] = "UCKfreQYtL6GZSj9Zq5FRQGA"
channelDict["Daniel Bourke"] = "UCr8O8l5cCX85Oem1d18EezQ"
channelDict["AI Guy"] = "UCrydcKaojc44XnuXrfhlV8Q"
channelDict["MLSS"] = "UCBOgpkDhQuYeVVjuzS5Wtxw"
channelDict["Matroid"] = "UCR85FcguqcxLQ7XEg1byAtQ"
channelDict["Saturn Cloud"] = "UCADT4bgaV94IVkpABEY7iiA"
channelDict["Altdeep"] = "UCopQd3S1UGsEwqs5Dy2kQwg"
channelDict["Robert Monarch"] = "UCjK2LOJJy9gomvzcfUFgdDA"
channelDict["CMU AI"] = "UCLh3OUmBGe4wPyVZiI771ng"













df_list = []

for name, channel_id in channelDict.items():

    url = "https://www.googleapis.com/youtube/v3/search?key="+yt_key + \
        "&channelId="+channel_id+"&part=snippet,id&order=date&maxResults=5&type=video"
    # print(url)
    print("fetching channel", name)
    from urllib.request import urlopen
    json_str = urlopen(url).read()
    df_list.append(pd.json_normalize(json.loads(json_str)["items"]))

df = pd.concat(df_list)
df.to_csv("videos.csv")
